import numpy as np

I = np.array([[1, 0],
              [0, 1]], dtype=complex)
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]], dtype=complex)
X = np.array([[0, 1],
              [1, 0]], dtype=complex)
Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

# CNOT gate (Control = Qubit 0, Target = Qubit 1)
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]], dtype=complex)

def create_two_qubit_state(q0_state='0', q1_state='0'):
    basis = {'0': np.array([1, 0], dtype=complex), 
             '1': np.array([0, 1], dtype=complex)}
    return np.kron(basis[q0_state], basis[q1_state])

def apply_1q_gate(gate, target_qubit):
    if target_qubit == 0:
        return np.kron(gate, I)
    elif target_qubit == 1:
        return np.kron(I, gate)
    else:
        raise ValueError("Target qubit must be 0 or 1")
    
def sample_measurements(statevector, shots=1000):
    probabilities = np.abs(statevector) ** 2
    basis_states = ['00', '01', '10', '11']
    
    samples = np.random.choice(basis_states, size=shots, p=probabilities)
    counts = {state: 0 for state in basis_states}
    for sample in samples:
        counts[sample] += 1
        
    return counts

def create_bell_states(initial_q0, initial_q1, label):
    print(f"\nCreating Bell state |{label}> from initial states |{initial_q0}{initial_q1}>")
    
    state = create_two_qubit_state(initial_q0, initial_q1)
    
    H_on_q0 = apply_1q_gate(H, target_qubit=0)
    state = H_on_q0 @ state
    
    state = CNOT @ state
    
    print(f"Statevector after creating |{label}>: {np.round(state, 4)}")
    
    shots = 1000
    results = sample_measurements(state, shots=shots)
    print(f"Measurement results after {shots} shots: ")
    for s, count in results.items():
        if count > 0:
            print(f"  |{s}>: {count} times ({(count/shots)*100:.2f}%)")
    print("\n")
    
if __name__ == "__main__":
    create_bell_states('0', '0', 'Φ+')
    create_bell_states('0', '1', 'Φ-')
    create_bell_states('1', '0', 'Ψ+')
    create_bell_states('1', '1', 'Ψ-')