import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function for theoretical temperature distribution
def T(Ta, T0, m, L, z):
    return Ta + (T0 - Ta) * (np.cosh(m * (L - z))) / np.cosh(m * L)

# Parameters
T0 = 100 + 273.15  # Initial temperature in Kelvin
h = 20  # Some constant related to heat transfer
B = 0.002  # Constant
K = 247  # Thermal conductivity or some other constant
m = h / (K * B/2)  # Calculate m
L = 0.07  # Length in meters
Ta = 20 + 273.15  # Ambient temperature in Kelvin

# Generate z values for theoretical plot
z_values = np.linspace(0, L, 100)
T_values = T(Ta, T0, m, L, z_values)

# Read data from the text file
data = pd.read_csv('D:/Desktop/data.txt', delim_whitespace=True, comment='%', skiprows=0, names=['Z', 'Y', 'T'])

# Extract Z and T from the data (ignore Y since it's small variations of 0, 0.001, etc.)
# We'll focus only on Z = 0 case (or average the small Y values if needed)
data_filtered = data[data['Y'] == 0]

Z_file = data_filtered['Z']
T_file = data_filtered['T']

# Plot both the theoretical and file data on the same plot
plt.plot(z_values, T_values, label='Theoretical T(z)', color='blue')
plt.plot(Z_file, T_file, label='Data from File T(Z)', color='red', linestyle='--')

# Add labels and title
plt.xlabel('z (m)')
plt.ylabel('T (K)')
plt.title('Temperature Distribution Comparison')
plt.grid(True)
plt.legend()

# Show plot
plt.show()
