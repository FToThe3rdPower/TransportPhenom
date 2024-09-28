import numpy as np
import matplotlib.pyplot as plt

def T(Ta, T0, m, L, z):
    T = Ta + (T0 - Ta)*(np.cosh(m*(L-z)))/np.cosh(m*L)
    return T

T0 = 100 + 273.15
h = 20
B = 0.002
K = 247
m = h/(K*B)
L = 0.07
Ta = 20 + 273.15

z_values = np.linspace(0, L, 100)


T_values = T(Ta, T0, m, L, z_values)

plt.plot(z_values, T_values)
plt.xlabel('z (m)')
plt.ylabel('T (K)')
plt.title('Temperature Distribution over Length')
plt.grid(True)
plt.show()