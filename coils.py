import numpy as np
import matplotlib.pyplot as plt

def magnetic_field_inside_solenoid(n, I, L, r, mu_0=4*np.pi*1e-7):
    B0 = mu_0 * n * I
    return B0

def field_variation(n, I, L, r, precision=0.05):
    mu_0 = 4 * np.pi * 1e-7
    B0 = magnetic_field_inside_solenoid(n, I, L, r, mu_0)
    
    z = np.linspace(-L/2, L/2, 1000)
    Bz = B0 * (1 - (z/(L/2))**2)
    
    mask = (Bz >= (1 - precision) * B0) & (Bz <= (1 + precision) * B0)
    uniform_region = z[mask]
    
    if len(uniform_region) > 0:
        uniform_length = uniform_region[-1] - uniform_region[0]
    else:
        uniform_length = 0

    fig, ax = plt.subplots()
    ax.plot(z, Bz, color='k', linewidth=2)
    ax.set_xlabel('Coordinate along the solenoid axis (m)')
    ax.set_ylabel('Magnetic field (T)')
    ax.set_title('Magnetic field distribution inside the solenoid')
    plt.show()

    return uniform_length

I = 1
L1 = 0.1
L2 = 0.01
r = 0.01
N1 = 1000
N2 = 100
n1 = N1 / L1
n2 = N2 / L2

uniform_length_1000 = field_variation(n1, I, L1, r)
uniform_length_100 = field_variation(n2, I, L2, r)

print(f"Uniformity region for 1000 turns: {uniform_length_1000:.3f} m")
print(f"Uniformity region for 100 turns: {uniform_length_100:.3f} m")
