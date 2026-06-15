import numpy as np

GATES = {
    'I': np.array([[1, 0],
                   [0, 1]], dtype=complex),
    'X': np.array([[0, 1],
                   [1, 0]], dtype=complex),
    'Y': np.array([[0, -1j],
                   [1j, 0]], dtype=complex),
    'Z': np.array([[1, 0],
                   [0, -1]], dtype=complex),
    'H': (1/np.sqrt(2)) * np.array([[1, 1],
                                     [1, -1]], dtype=complex),
    'S': np.array([[1, 0],
                   [0, 1j]], dtype=complex),
    'T': np.array([[1, 0],
                   [0, np.exp(1j * np.pi / 4)]], dtype=complex)
}

def create_qubit(state='0'):
    if state == '0':
        return np.array([1, 0], dtype=complex)
    if state == '1':
        return np.array([0, 1], dtype=complex)
    raise ValueError("Initial state must be '0' or '1'")

def apply_gate(qubit, gate):
    if gate not in GATES:
        raise ValueError(f"Gate {gate} not found.")
    return GATES[gate] @ qubit

def print_state_and_probs(qubit_state, label="Current State"):
    probablilites = np.abs(qubit_state) ** 2
    prob_0 = probablilites[0]
    prob_1 = probablilites[1]
    print(f"Statevector: [α, β]:\n {np.round(qubit_state, 4)}")
    print(f"Probability of measuring 0: {prob_0:.4f}")
    print(f"Probability of measuring 1: {prob_1:.4f}")
    
    
if __name__ == "__main__":
    qubit = create_qubit('0')
    print_state_and_probs(qubit, "Initial State |0>")
    
    qubit = apply_gate(qubit, 'H')
    print_state_and_probs(qubit, "After applying H gate")
    
    qubit = apply_gate(qubit, 'Z')
    print_state_and_probs(qubit, "After applying Pauli-Z gate")
    
    
        