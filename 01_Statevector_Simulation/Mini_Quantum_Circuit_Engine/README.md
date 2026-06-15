# Mini Quantum Circuit Engine

A lightweight, class-based quantum circuit simulator built purely with NumPy.

This project abstracts the raw matrix math of quantum statevectors into a programmable object-oriented interface. It generalizes the tensor product arithmetic to allow operations on systems of $n$ qubits without hardcoding massive unitary matrices.

## What it does

1. Implements a `QuantumCircuit(n)` class that initializes a $2^n$ dimensional statevector.
2. Dynamically pads single-qubit gates (`H`, `X`, `Z`) with Identity matrices using `np.kron` to apply them to specific target qubits.
3. Constructs arbitrary `CNOT` gates dynamically using projection matrices ($|0\rangle\langle0|$ and $|1\rangle\langle1|$), allowing entanglement between any two qubits in the register.
4. Samples the probability distribution dictated by the statevector to simulate real quantum measurement.

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)

## Usage

Run the script to see the engine reproduce both a single-qubit superposition and a two-qubit maximally entangled Bell state:

```bash
python circuit_engine.py
```
