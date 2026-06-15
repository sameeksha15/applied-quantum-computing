# Two-Qubit Entanglement Demo

A raw NumPy implementation extending single-qubit quantum simulation to a two-qubit system.

This project strips away the mystery of quantum entanglement by calculating it directly. It utilizes the tensor product (`np.kron`) to expand the state space to $4 \times 1$ vectors and implements the CNOT gate as a $4 \times 4$ unitary matrix.

## What it does

1. Initializes two independent qubits and combines them into a single statevector using the tensor product.
2. Implements a function to tensor $2 \times 2$ single-qubit gates with the Identity matrix, allowing them to act on a two-qubit system.
3. Applies a Hadamard gate and a CNOT gate to generate all four maximally entangled Bell states ($|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle$).
4. Simulates quantum measurement by sampling the final statevector $1000$ times based on the Born rule probabilities.

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)

## Usage

Run the script to see the generation of the four Bell states and the resulting perfect correlations in the simulated measurements:

```bash
python qubit_entanglement.py
```
