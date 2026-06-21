# Superdense Coding Simulation with Qiskit

## Overview

This project demonstrates the **Superdense Coding** quantum communication protocol using IBM's Qiskit framework. Superdense coding achieves the complementary goal of quantum teleportation: it allows a sender (**Alice**) to transmit **two classical bits of information** to a receiver (**Bob**) by sending only **one quantum bit (qubit)**, provided they share a pre-existing entangled qubit pair (an **e-bit**).

This protocol highlights a striking application of quantum entanglement. By circumventing **Holevo's theorem** which dictates that one qubit can typically only carry one bit of classical information—superdense coding effectively doubles the classical information-carrying capacity of a single qubit.

## Background

The protocol relies on the four **Bell states** (maximally entangled two-qubit states). Alice and Bob initially share the Bell state **|ϕ⁺⟩**. Depending on the two classical bits (**c** and **d**) Alice wants to send, she applies a specific quantum gate to her portion of the entangled pair:

- **00**: Apply Identity (**I**) → State remains **|ϕ⁺⟩**
- **01**: Apply Pauli-Z (**Z**) → State becomes **|ϕ⁻⟩**
- **10**: Apply Pauli-X (**X**) → State becomes **|ψ⁺⟩**
- **11**: Apply Pauli-X and Pauli-Z (**XZ**) → State becomes **|ψ⁻⟩**

Alice then sends her single qubit to Bob. Bob performs a deterministic decoding sequence (a **CNOT** gate followed by a **Hadamard** gate) and measures both qubits. The measurement collapses the chosen Bell state exactly into the corresponding two classical bits Alice intended to send.

## Project Structure

The Jupyter Notebook (`superdense_coding.ipynb`) is divided into two primary simulations:

### 1. Deterministic Transmission (Hardcoded Bits)

- A simple, two-qubit circuit where Alice's bits are hardcoded to **c = 1** and **d = 0**.
- Demonstrates the fundamental gate operations (entanglement preparation, Alice's encoding, Bob's decoding).
- Verifies that Bob correctly receives the message **10** with **100% certainty**.

### 2. Randomized Transmission (Coin Flip)

- A more advanced five-register circuit using dynamic classical conditioning.
- Introduces a third "coin" qubit to randomly generate Alice's classical bits.
- Alice encodes her bits using `if_test` (classical control) operations.
- Bob decodes and measures. The results verify that regardless of the random bits generated, Bob's measured bits always perfectly match Alice's generated bits.

## Prerequisites & Dependencies

To run this notebook, you will need Python installed along with the following libraries:

- `qiskit`
- `qiskit-aer`
- `matplotlib`
- `numpy`

Install the dependencies using pip:

```bash
pip install qiskit qiskit-aer matplotlib numpy
```
