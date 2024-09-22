import numpy as np
import matplotlib.pyplot as plt

### PART 1: for Velocity and Stress Calculations ###

def constants(r, R1, R2, U, mu, Qw):
    J = ((((R1**4)/4) - ((R2**4)/4)) * np.log(R2/R1)) + (((R2**2)/2)  - ((R1**2)/2))**2
    dpdz = ((2 * mu * np.log(R2 / R1)) / (np.pi * J)) * (Qw + (((2 * np.pi * U) / np.log(R1 / R2)) * 
            ((((R1**2) / 2) * np.log(R1 / R2)) + ((R2**2) / 4) - ((R1**2) / 4))))
    return J, dpdz

def vr_1(r, R1, R2, U, mu, Qw):
    J, dpdz = constants(r, R1, R2, U, mu, Qw)
    v_z = ((-1 * dpdz) * (((R2**2) - (r**2)) / (4 * mu))) + ((U + (dpdz * (((R2**2) - (R1**2)) / (4 * mu)))) * 
            ((np.log(R2 / r)) / (np.log(R2 / R1))))
    return v_z

def trz_1(r, R1, R2, U, mu, Qw):
    J, dpdz = constants(r, R1, R2, U, mu, Qw)
    t_rz = ((-1 * dpdz) * (r / 2)) + ((U + (dpdz * (((R2**2) - (R1**2)) / (4 * mu)))) * 
            ((mu / (np.log(R2 / R1))) * (1 / r)))
    return t_rz

### PART 1: Plotting Functions ###
def vel_plot_1(r, R1, R2, U, mu, Qw, Qw_, r_mm, label_name):
    plt.plot(r_mm, vr_1(r, R1, R2, U, mu, Qw), label=f"{label_name}")
    plt.title("Velocity Profile for Cylindrical Geometry", fontsize=14)
    plt.xlabel("Radial Distance [mm]", fontsize=12)
    plt.ylabel("Axial Velocity [m/s]", fontsize=12)
    plt.grid(True)
    plt.legend()
    return

def stress_plot_1(r, R1, R2, U, mu, Qw, Qw_, r_mm):
    plt.plot(r_mm, trz_1(r, R1, R2, U, mu, Qw), label=f"{Qw_} [ml/min]")
    plt.title("Shear Stress Profile for Cylindrical Geometry", fontsize=14)
    plt.xlabel("Radial Distance [mm]", fontsize=12)
    plt.ylabel("Shear Stress [N/m²]", fontsize=12)
    plt.grid(True)
    plt.legend()
    return

### PART 2: for Alternative Model ###

def vr_2(r, R1, R2, U, mu, Qw, w1, w2):
    v_z = ((R2**2) / ((R2**2) - (R1**2))) * (((w2 - ((w1 * (R1**2)) / (R2**2))) * r) - (((w2 - w1) * (R1**2)) / r))
    return v_z

def trz_2(r, R1, R2, U, mu, Qw, w1, w2, value):
    t_rz = value * (((2 * mu * (R1**2) * (R2**2) * (w2 - w1)) / ((R2**2) - (R1**2))) * (r**(-2)))
    return t_rz

### PART 2: Plotting Functions ###
def vel_plot_2(r, R1, R2, U, mu, Qw, Qw_, r_mm, w1, w2):
    plt.plot(r_mm, vr_2(r, R1, R2, U, mu, Qw, w1, w2), label="Analytical Solution")
    plt.title("Velocity Profile for Analytical Model", fontsize=14)
    plt.xlabel("Radial Distance [mm]", fontsize=12)
    plt.ylabel("Velocity [rad/s]", fontsize=12)
    plt.grid(True)
    plt.legend()
    return

def stress_plot_2(r, R1, R2, U, mu, Qw, Qw_, r_mm, w1, w2, value):
    plt.plot(r_mm, trz_2(r, R1, R2, U, mu, Qw, w1, w2, value), label="Analytical Solution")
    plt.title("Shear Stress Profile for Analytical Model", fontsize=14)
    plt.xlabel("Radial Distance [mm]", fontsize=12)
    plt.ylabel("Shear Stress [N/m²]", fontsize=12)
    plt.grid(True)
    plt.legend()
    return

