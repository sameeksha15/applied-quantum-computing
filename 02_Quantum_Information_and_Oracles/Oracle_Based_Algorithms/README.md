# Oracle Based Algorithms: Deutsch and Deutsch-Jozsa

This folder contains Qiskit implementations of two foundational quantum query algorithms: **Deutsch's Algorithm** and the **Deutsch-Jozsa Algorithm**.

These algorithms demonstrate some of the earliest examples of a quantum computational advantage, solving specific function-evaluation problems using fewer oracle queries than their classical counterparts.

---

# 1. Deutsch's Algorithm

Deutsch's Algorithm solves a specialized parity problem for a single-bit input (`n = 1`). It determines whether a given black-box function (oracle) is **constant** or **balanced** using only **one query**.

## The Problem

We are given a function:

$$
f:\{0,1\} \rightarrow \{0,1\}
$$

There are exactly four possible functions:

| Function | f(0) | f(1) | Category |
| -------- | ---- | ---- | -------- |
| $f_1$    | 0    | 0    | Constant |
| $f_2$    | 0    | 1    | Balanced |
| $f_3$    | 1    | 0    | Balanced |
| $f_4$    | 1    | 1    | Constant |

### Definitions

- **Constant**: The output is identical for every input.
- **Balanced**: Half of the inputs map to 0 and half map to 1.

### Goal

Determine whether $f$ is **constant** or **balanced**.

### Classical Approach

A deterministic classical algorithm must evaluate both:

$$
f(0), \quad f(1)
$$

requiring **2 oracle queries**.

### Quantum Approach

Deutsch's Algorithm determines the answer with only **1 oracle query**.

---

## How It Works: Phase Kickback

The quantum advantage arises from a phenomenon known as **phase kickback**.

### Step 1: Initialization

Prepare two qubits in the state:

$$
|1\rangle|0\rangle
$$

(Qiskit displays qubits in reverse order, so this corresponds to the top and bottom wires respectively.)

### Step 2: Create Superposition

Apply Hadamard gates to both qubits:

$$
|\psi_1\rangle = |-\rangle|+\rangle
$$

where

$$
|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}
$$

$$
|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

### Step 3: Oracle Application

Apply the oracle $U_f$.

Instead of simply flipping the target qubit, the oracle transfers the function value into the phase:

$$
U_f(|-\rangle|a\rangle)
=
(-1)^{f(a)}
|-\rangle|a\rangle
$$

This is the phase kickback effect.

After simplification, the state becomes:

$$
|\psi_2\rangle
=
(-1)^{f(0)}
|-\rangle
\left(
\frac{|0\rangle + (-1)^{f(0)\oplus f(1)}|1\rangle}{\sqrt{2}}
\right)
$$

### Step 4: Interference

Apply a final Hadamard gate.

The resulting state depends on:

$$
f(0)\oplus f(1)
$$

- If $f(0)\oplus f(1)=0$ (constant), the qubit becomes:

$$
|0\rangle
$$

- If $f(0)\oplus f(1)=1$ (balanced), the qubit becomes:

$$
|1\rangle
$$

### Step 5: Measurement

Measure the query qubit.

| Measurement | Function Type |
| ----------- | ------------- |
| 0           | Constant      |
| 1           | Balanced      |

Thus, a single oracle query determines the answer.

---

# 2. Deutsch-Jozsa Algorithm

The Deutsch-Jozsa Algorithm generalizes Deutsch's Algorithm to an arbitrary number of input bits.

It provides an **exponential separation** between deterministic classical and quantum query complexity.

---

## The Problem

Given a function:

$$
f:\{0,1\}^n \rightarrow \{0,1\}
$$

that accepts an $n$-bit string and returns a single bit.

### Promise

The function is guaranteed to be either:

#### Constant

$$
f(x)=0 \quad \forall x
$$

or

$$
f(x)=1 \quad \forall x
$$

#### Balanced

Exactly half of all possible inputs produce 0 and half produce 1.

---

## Goal

Determine whether $f$ is:

- Constant → Output **0**
- Balanced → Output **1**

---

## Classical Complexity

A deterministic classical algorithm may need:

$$
2^{n-1}+1
$$

queries in the worst case.

For example, if the first $2^{n-1}$ evaluations all return 0, one additional query is needed to be certain.

### Probabilistic Classical Algorithms

Randomized algorithms can achieve high confidence with relatively few queries.

For example:

- 11 random queries provide over 99.9% confidence.

However, certainty still requires exponentially many queries.

---

## Quantum Complexity

Deutsch-Jozsa solves the problem with:

$$
1
$$

oracle query, regardless of $n$.

---

## How It Works

### Step 1: Initialization

Prepare:

- $n$ query qubits in $|0\rangle$
- 1 ancilla qubit in $|1\rangle$

$$
|0\rangle^{\otimes n}|1\rangle
$$

---

### Step 2: Create Superposition

Apply Hadamard gates to all qubits.

The query register becomes:

$$
H^{\otimes n}|0\dots0\rangle
=
\frac{1}{\sqrt{2^n}}
\sum_{x\in\{0,1\}^n}
|x\rangle
$$

This creates an equal superposition over all possible inputs.

---

### Step 3: Oracle Evaluation

Apply the oracle $U_f$.

Through phase kickback:

$$
|x\rangle
\rightarrow
(-1)^{f(x)}
|x\rangle
$$

The resulting state is:

$$
\frac{1}{\sqrt{2^n}}
\sum_x
(-1)^{f(x)}
|x\rangle
$$

---

### Step 4: Interference

Apply another layer of Hadamard gates to the query register.

The amplitudes interfere according to the structure of the function.

---

### Step 5: Measurement

Measure the $n$ query qubits.

#### Constant Function

All amplitudes interfere constructively.

The state collapses to:

$$
|00\dots0\rangle
$$

with probability 1.

#### Balanced Function

Positive and negative amplitudes cancel perfectly.

The probability of measuring

$$
|00\dots0\rangle
$$

is exactly 0.

At least one measured bit will be 1.

---

## Decision Rule

| Measurement Result | Function Type |
| ------------------ | ------------- |
| $00\dots0$         | Constant      |
| Anything else      | Balanced      |

Thus, a single oracle query is sufficient to determine the answer with **100% certainty**.

# Prerequisites

Install the required packages:

```bash
pip install numpy qiskit qiskit-aer matplotlib
```

# Key Concepts Demonstrated

- Quantum Superposition
- Quantum Interference
- Phase Kickback
- Quantum Oracles
- Query Complexity
- Exponential Quantum Advantage
- Hadamard Transform
- Deterministic Quantum Algorithms
