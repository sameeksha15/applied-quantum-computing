# Quantum Teleportation Using Qiskit

## Concept

Quantum Teleportation is a protocol by which quantum information (the exact quantum state of a qubit) can be transmitted from one location to another. It requires a classical communication channel and a previously shared pair of entangled qubits between the sending and receiving locations.

Importantly, it is the _information_ that is teleported, not the physical qubit itself. Furthermore, the original state is destroyed in the process, adhering to the fundamental **No-Cloning Theorem** of quantum mechanics.

## The Scenario

Imagine **Alice** wants to send a secret quantum payload to **Bob**.

1. **Entanglement Setup:** Alice and Bob share an entangled pair of qubits (a Bell state). Alice holds one qubit, and Bob holds the other.
2. **Alice's Operations:** Alice takes the "secret" qubit she wishes to teleport and entangles it with her half of the shared entangled pair. She then measures both her secret qubit and her entangled qubit.
3. **Classical Communication:** Alice's measurement collapses her qubits, yielding two classical bits (e.g., `00`, `01`, `10`, or `11`). She sends these two classical bits to Bob over a standard communication channel.
4. **Bob's Correction:** Based on the two bits he receives, Bob applies a specific set of quantum operations (Pauli-X and/or Pauli-Z gates) to his half of the entangled pair.
5. **Completion:** After the corrective operations, Bob's qubit assumes the exact quantum state of the original secret qubit.

## Project Execution & Details

The `teleportation.ipynb` notebook implements this protocol step-by-step:

- **Random State Generation:** We initialize the secret qubit with a random state using a parameterized unitary gate ($U$ gate).
- **Protocol Implementation:** We create a Bell state between Alice and Bob's qubits, apply Alice's entangling operations and measurements, and use `if_test` to apply Bob's conditional phase and bit flips.
- **Ideal Verification:** To prove teleportation was successful, we apply the _inverse_ of the initial unitary gate to Bob's qubit. Measuring it at the end should yield `0` perfectly on an ideal simulator (`AerSimulator`).
- **Noisy Simulation:** We introduce real-world effects by running the circuit on a simulated noisy hardware profile (`GenericBackendV2`). A side-by-side histogram comparison highlights the impact of quantum noise on the fidelity of the teleportation.
- **Visualizing State Evolution:** Using Qiskit's `Statevector` and `plot_bloch_multivector`, we visualize the qubits on Bloch spheres at 3 specific stages:
  1. The initial generated Payload.
  2. The Entangled phase.
  3. The Completion phase (showing Bob's qubit acquiring the state and Alice's original state being destroyed).
