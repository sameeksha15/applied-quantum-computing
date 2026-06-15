import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

def state_to_bloch_coords(state):
    alpha, beta = state
    
    # 1. Normalize the state (to ensure it lies exactly on the sphere)
    norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    alpha, beta = alpha / norm, beta / norm
    
    # 2. Remove the global phase 
    phase_alpha = np.angle(alpha)
    alpha_real = np.abs(alpha)
    beta_adjusted = beta * np.exp(-1j * phase_alpha)
    
    # 3. Calculate the angles for the Bloch sphere
    theta = 2 * np.arccos(alpha_real)
    phi = np.angle(beta_adjusted)
    
    # 4. Convert to Cartesian coordinates
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    return x, y, z

def plot_bloch_sphere(state, title="Qubit State on Bloch Sphere"):
    x, y, z = state_to_bloch_coords(state)
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    sphere_x = np.cos(u) * np.sin(v)
    sphere_y = np.sin(u) * np.sin(v)
    sphere_z = np.cos(v)
    ax.plot_wireframe(sphere_x, sphere_y, sphere_z, color="gray", alpha=0.15)
    
    # Draw the axes (X, Y, Z)
    ax.plot([-1.2, 1.2], [0, 0], [0, 0], color='black', linewidth=0.8)
    ax.plot([0, 0], [-1.2, 1.2], [0, 0], color='black', linewidth=0.8)
    ax.plot([0, 0], [0, 0], [-1.2, 1.2], color='black', linewidth=0.8)
    
    # Label the axes and poles
    ax.text(1.3, 0, 0, 'x', fontsize=12)
    ax.text(0, 1.3, 0, 'y', fontsize=12)
    ax.text(0, 0, 1.2, '|0>', fontsize=12, ha='center')
    ax.text(0, 0, -1.3, '|1>', fontsize=12, ha='center')
    
    # Plot the state vector as an arrow
    ax.quiver(0, 0, 0, x, y, z, color='red', arrow_length_ratio=0.1, linewidth=2.5)
    ax.scatter(x, y, z, color='red', s=50) # Point at the end of the arrow
    
    # Formatting
    ax.set_title(title)
    ax.set_box_aspect([1, 1, 1]) # Ensure it looks like a sphere, not an ellipsoid
    ax.axis('off')               # Hide the default Matplotlib 3D grid
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    state_0 = np.array([1, 0], dtype=complex)  # |0>
    plot_bloch_sphere(state_0, "State |0>")

    state_plus = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
    plot_bloch_sphere(state_plus, "State |+>")
    
    state_i = np.array([1/np.sqrt(2), 1j/np.sqrt(2)], dtype=complex)
    plot_bloch_sphere(state_i, "State |i>")
    
    

    
    