# Single Qubit Gate Simulator

A lightweight, strictly NumPy-based simulator for single-qubit quantum gates.

This project is a raw mathematical translation of quantum mechanics into Python code. It avoids high-level quantum frameworks (like Qiskit) to demonstrate how statevectors, unitary matrices, and probability amplitudes function under the hood.

## What it does

1. Represents a qubit as a complex NumPy array `[α, β]`.
2. Implements standard single-qubit gates (`H`, `X`, `Y`, `Z`, `S`, `T`) as $2 \times 2$ matrices.
3. Applies gates using matrix multiplication.
4. Calculates the probability of measuring a `0` or `1` state using the Born rule ($|\alpha|^2$ and $|\beta|^2$).

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)

## Usage

Run the simulator directly from the command line:

```bash
python simulator.py
```
