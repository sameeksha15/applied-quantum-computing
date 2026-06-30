# Applied Quantum Computing

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Applied Quantum Computing is a collection of small, hands-on quantum computing demos built with Python, NumPy, and Qiskit. The repo is organized as a learning workspace: each folder focuses on one concept, with scripts and notebooks that show the math, the circuit construction, and the resulting measurements.

## What the project does

The project currently covers two main areas:

- Statevector simulation and low-level quantum mechanics with NumPy.
- Quantum information demos and algorithm notebooks built with Qiskit.

The current workspace includes:

- [Single Qubit Gate Simulator](01_Statevector_Simulation/Single_Qubit_Gate_Simulator/README.md)
- [Mini Quantum Circuit Engine](01_Statevector_Simulation/Mini_Quantum_Circuit_Engine/README.md)
- [Bloch Sphere Visualizer](01_Statevector_Simulation/Bloch_Sphere_Visualizer/README.md)
- [Two-Qubit Entanglement Demo](01_Statevector_Simulation/Two_Qubit_Entanglement/README.md)
- [Bell States Explorer](02_Quantum_Information_and_Oracles/Bell_States_Explorer/README.md)
- [Quantum Teleportation](02_Quantum_Information_and_Oracles/Quantum_Teleportation/README.md)
- [Superdense Coding](02_Quantum_Information_and_Oracles/Superdense_Coding/README.md)
- [Oracle Based Algorithms](02_Quantum_Information_and_Oracles/Oracle_Based_Algorithms/README.md)

## Why the project is useful

This repo is designed to make quantum computing concepts concrete and interactive. It is useful if you want to:

- Understand qubits, superposition, measurement, and entanglement from first principles.
- Compare raw NumPy implementations with higher-level Qiskit circuits.
- Explore canonical quantum protocols such as Bell states, teleportation, superdense coding, and Deutsch-Jozsa style oracle problems.
- Use notebooks and scripts as a study companion while learning quantum computing.

## How to get started

### Prerequisites

- Python 3.10 or newer
- `pip`
- VS Code with the Jupyter extension, or a local Jupyter environment

### Install dependencies

From the repository root, install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Where to get help

Start with the most relevant project-level README for the demo you are running. The folder READMEs explain the concept, the code path, and the expected output for each example.

- [Root license](LICENSE)
- [Quantum teleportation notes](02_Quantum_Information_and_Oracles/Quantum_Teleportation/README.md)
- [Bell states explorer notes](02_Quantum_Information_and_Oracles/Bell_States_Explorer/README.md)
- [Oracle algorithms notes](02_Quantum_Information_and_Oracles/Oracle_Based_Algorithms/README.md)
