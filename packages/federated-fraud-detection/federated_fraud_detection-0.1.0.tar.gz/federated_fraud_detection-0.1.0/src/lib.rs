use std::ops::{BitXor, BitXorAssign};

use curve25519_dalek::{scalar::Scalar, constants::RISTRETTO_BASEPOINT_TABLE, ristretto::{CompressedRistretto, RistrettoPoint, RistrettoBasepointTable}};
use pyo3::{prelude::*, types::{PyBytes, PyTuple}};
use rand::thread_rng;
use okvs::{schemes::{Okvs, paxos::Paxos}, hashable::Hashable, bits::Bits};

// TODO: Consider returning Vecs instead of bytes

/// Generates a key pair for this party, returning a tuple with (public_key: bytes, secret_key: bytes).
#[pyfunction]
fn key_gen(py: Python) -> &PyTuple {
    let sk = Scalar::random(&mut thread_rng());
    let pk = &sk * &RISTRETTO_BASEPOINT_TABLE;

    let pk_bytes = pk.compress().as_bytes().to_vec();
    let sk_bytes = sk.as_bytes().to_vec();

    let pk_object: PyObject = PyBytes::new(py, &pk_bytes).into();
    let sk_object: PyObject = PyBytes::new(py, &sk_bytes).into();

    PyTuple::new(py, [pk_object, sk_object])
}

#[derive(Debug, PartialEq)]
struct DataRow(Vec<String>);

impl Hashable for DataRow {
    fn to_bytes(&self) -> Vec<u8> {
        self.0.iter().flat_map(|x| x.as_bytes()).copied().collect()
    }
}

#[derive(Debug, Clone, Copy)]
struct Ciphertext {
    c1: [u8; 32],
    c2: [u8; 32],
}

impl Ciphertext {
    pub fn zero(public_key_table: &RistrettoBasepointTable) -> Self {
        let randomness = Scalar::random(&mut thread_rng());

        Self {
            c1: (&randomness * &RISTRETTO_BASEPOINT_TABLE).compress().to_bytes(),
            c2: (&randomness * public_key_table).compress().to_bytes(),
        }
    }

    pub fn add_and_randomize(ciphertext_a: Self, ciphertext_b: Self) -> WideCiphertext {
        let randomness = Scalar::random(&mut thread_rng());

        let point_a_c1 = CompressedRistretto::from_slice(&ciphertext_a.c1).decompress().expect("C1 of ciphertext A was not a valid curve point.");
        let point_a_c2 = CompressedRistretto::from_slice(&ciphertext_a.c2).decompress().expect("C2 of ciphertext A was not a valid curve point.");
        let point_b_c1 = CompressedRistretto::from_slice(&ciphertext_b.c1).decompress().expect("C1 of ciphertext B was not a valid curve point.");
        let point_b_c2 = CompressedRistretto::from_slice(&ciphertext_b.c2).decompress().expect("C2 of ciphertext B was not a valid curve point.");

        // Represents the sum of the two ciphertexts multiplied by some random scalar.
        // FIXME: We should also add two encryptions of 0 of SWIFT
        WideCiphertext {
            c1a: (&randomness * &point_a_c1).compress().to_bytes(),
            c1b: (&randomness * &point_b_c1).compress().to_bytes(),
            c2: (&randomness * &(point_a_c2 + point_b_c2)).compress().to_bytes(),
        }
    }
}

impl Bits for Ciphertext {
    fn random() -> Self {
        // TODO: This can be done cheaper by generating random bytes and masking a bit.
        Self {
            c1: RistrettoPoint::random(&mut thread_rng()).compress().to_bytes(),
            c2: RistrettoPoint::random(&mut thread_rng()).compress().to_bytes(),
        }
    }
}

impl BitXor for Ciphertext {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        todo!()
    }
}

impl BitXorAssign for Ciphertext {
    fn bitxor_assign(&mut self, rhs: Self) {
        todo!()
    }
}

/// Contains c1 for parties A and B as c1a and c1b. This enables the final decryption.
struct WideCiphertext {
    c1a: [u8; 32],
    c1b: [u8; 32],
    c2: [u8; 32]
}

impl WideCiphertext {
    fn randomize(self) -> Self {
        todo!()
    }

    fn to_bytes(self) -> Vec<u8> {
        let mut bytes = self.c1a.to_vec();
        bytes.extend(self.c1b);
        bytes.extend(self.c2);

        bytes
    }

    fn from_bytes(bytes: &[u8]) -> Self {
        todo!()
    }
}

fn read_public_key(py: Python, public_key: PyObject) -> RistrettoPoint {
    let public_key_bytes: &PyBytes = public_key.cast_as(py).expect("The public key object should be of type `bytes`.");
    CompressedRistretto::from_slice(public_key_bytes.as_bytes()).decompress().expect("The public key was not a valid curve point.")
}

/// Builds an OKVS for one party. Takes the public key of this party and the data from the database, which is a list of rows. Each row is a list of the relevant columns as a String.
#[pyfunction]
fn build_okvs(py: Python, public_key: PyObject, strings_in_each_row: Vec<Vec<String>>) -> PyObject {
    let public_key_table = RistrettoBasepointTable::create(&read_public_key(py, public_key));

    let data_rows: Vec<(DataRow, Ciphertext)> = strings_in_each_row.into_iter().map(|row| (DataRow(row), Ciphertext::zero(&public_key_table))).collect();

    let okvs: Paxos<Ciphertext> = Paxos::encode(&data_rows, 40);

    PyBytes::new(py, &okvs.to_bytes()).into()
}

// TODO: Parallelize
#[pyfunction]
fn initiate_queries(py: Python, sender_data: Vec<Vec<String>>, receiver_data: Vec<Vec<String>>, sender_okvs: PyObject, receiver_okvs: PyObject, swift_sk: PyObject) -> PyObject {
    let sender_okvs_bytes: &PyBytes = sender_okvs.cast_as(py).expect("The sender_okvs object should be of type `bytes`.");
    let sender_okvs_instance: Paxos<Ciphertext> = Paxos::from_bytes(sender_okvs_bytes.as_bytes());
    let sender_ciphertexts: Vec<Ciphertext> = sender_data.into_iter().map(|row| sender_okvs_instance.decode(&DataRow(row))).collect();

    let receiver_okvs_bytes: &PyBytes = receiver_okvs.cast_as(py).expect("The receiver_okvs object should be of type `bytes`.");
    let receiver_okvs_instance: Paxos<Ciphertext> = Paxos::from_bytes(receiver_okvs_bytes.as_bytes());
    let receiver_ciphertexts: Vec<Ciphertext> = receiver_data.into_iter().map(|row| receiver_okvs_instance.decode(&DataRow(row))).collect();

    let aggregated_ciphertexts: Vec<u8> = sender_ciphertexts.into_iter().zip(receiver_ciphertexts).flat_map(|(cs, cr)| Ciphertext::add_and_randomize(cs, cr).to_bytes()).collect();

    PyBytes::new(py, &aggregated_ciphertexts).into()
}

#[pyfunction]
fn randomize(py: Python, ciphertexts: PyObject) -> PyObject {
    let ciphertexts_bytes: &PyBytes = ciphertexts.cast_as(py).expect("The ciphertexts object should be of type `bytes`.");
    let randomized_ciphertexts: Vec<u8> = ciphertexts_bytes.as_bytes().chunks(96).flat_map(|chunk| WideCiphertext::from_bytes(chunk).randomize().to_bytes()).collect();

    PyBytes::new(py, &randomized_ciphertexts).into()
}

#[pyfunction]
fn combine(py: Python, sender_ciphertexts: PyObject, receiver_ciphertexts: PyObject) -> PyObject {
    let sender_ciphertexts_bytes: &PyBytes = sender_ciphertexts.cast_as(py).expect("The sender_ciphertexts object should be of type `bytes`.");
    let receiver_ciphertexts_bytes: &PyBytes = receiver_ciphertexts.cast_as(py).expect("The receiver_ciphertexts object should be of type `bytes`.");

    //let randomized_ciphertexts: Vec<u8> = ciphertexts_bytes.as_bytes().chunks(96).flat_map(|chunk| WideCiphertext::from_bytes(chunk).randomize().to_bytes()).collect();

    //PyBytes::new(py, &randomized_ciphertexts).into()
    todo!()
}

#[pyfunction]
fn decrypt(py: Python, points: PyObject, bank_secret_key: PyObject) -> PyObject {
    let points_bytes: &PyBytes = points.cast_as(py).expect("The points object should be of type `bytes`.");
    //let randomized_ciphertexts: Vec<u8> = ciphertexts_bytes.as_bytes().chunks(96).flat_map(|chunk| WideCiphertext::from_bytes(chunk).randomize().to_bytes()).collect();

    //PyBytes::new(py, &randomized_ciphertexts).into()
    todo!()
}

#[pyfunction]
fn finish(py: Python, sender_points: PyObject, receiver_points: PyObject, swift_secret_key: PyObject) -> PyObject {
    //let points_bytes: &PyBytes = points.cast_as(py).expect("The points object should be of type `bytes`.");
    //let randomized_ciphertexts: Vec<u8> = ciphertexts_bytes.as_bytes().chunks(96).flat_map(|chunk| WideCiphertext::from_bytes(chunk).randomize().to_bytes()).collect();

    //PyBytes::new(py, &randomized_ciphertexts).into()
    todo!()
}

/// A Python module for the cryptographic operations necessary to do feature extraction (element matching in two datasets).
#[pymodule]
fn federated_fraud_detection(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(key_gen, m)?)?;
    m.add_function(wrap_pyfunction!(build_okvs, m)?)?;
    m.add_function(wrap_pyfunction!(initiate_queries, m)?)?;
    m.add_function(wrap_pyfunction!(randomize, m)?)?;
    m.add_function(wrap_pyfunction!(combine, m)?)?;
    m.add_function(wrap_pyfunction!(decrypt, m)?)?;
    m.add_function(wrap_pyfunction!(finish, m)?)?;
    Ok(())
}
