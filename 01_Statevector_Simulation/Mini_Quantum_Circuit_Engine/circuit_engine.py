import numpy as np

class QuantumCircuit:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits
        
        self.state = np.zeros(2 ** n_qubits, dtype=complex)
        self.state[0] = 1.0
        
        self.I = np.array([[1, 0],
                           [0, 1]], dtype=complex)
        self.X = np.array([[0, 1],
                           [1, 0]], dtype=complex)
        self.Z = np.array([[1, 0],
                           [0, -1]], dtype=complex)
        self.H = (1/np.sqrt(2)) * np.array([[1, 1],
                                            [1, -1]], dtype=complex)
        self.gates = {
            'I': self.I,
            'X': self.X,
            'Z': self.Z,
            'H': self.H
        }
        
    def apply_1q_gate(self, gate_name, target_qubit):
        gate = self.gates[gate_name]
        
        ops = [gate if i == target_qubit else self.I for i in range(self.n_qubits)]
        
        operator = ops[0]
        for op in ops[1:]:
            operator = np.kron(operator, op)
            
        self.state = operator @ self.state
        
    def apply_cnot(self, control_qubit, target_qubit):
        P0 = np.array([[1, 0],
                      [0, 0]], dtype=complex)
        P1 = np.array([[0, 0],
                       [0, 1]], dtype=complex)
        
        ops_term1 = [self.I] * self.n_qubits
        ops_term1[control_qubit] = P0
        
        ops_term2 = [self.I] * self.n_qubits
        ops_term2[control_qubit] = P1
        ops_term2[target_qubit] = self.X
        
        def build_operator(ops_list):
            op = ops_list[0]
            for o in ops_list[1:]:
                op = np.kron(op, o)
            return op
        
        cnot_operator = build_operator(ops_term1) + build_operator(ops_term2)
        self.state = cnot_operator @ self.state
        
    def measure(self, shots=1000):
        probabilities = np.abs(self.state) ** 2
        basis_states = [format(i, f'0{self.n_qubits}b') for i in range(2 ** self.n_qubits)]
        samples = np.random.choice(basis_states, size=shots, p=probabilities)
        
        counts = {state: 0 for state in basis_states}
        for sample in samples:
            counts[sample] += 1
            
        return counts
    
if __name__ == "__main__":
    print("Project 1: Single Qubit Hadamard")
    qc1 = QuantumCircuit(1)
    qc1.apply_1q_gate('H', 0)
    print(f"Statevector: {np.round(qc1.state, 4)}")
    print(f"Measurements (1000 shots): {qc1.measure()}\n")

    print("Project 3: Two-Qubit Bell State (Phi+)")
    qc2 = QuantumCircuit(2)
    qc2.apply_1q_gate('H', 0)
    qc2.apply_cnot(control_qubit=0, target_qubit=1)
    print(f"Statevector: {np.round(qc2.state, 4)}")
    
    results2 = qc2.measure()
    print("Measurements (1000 shots):")
    for state, count in results2.items():
        if count > 0:
            print(f" |{state}> : {count}")
            
        