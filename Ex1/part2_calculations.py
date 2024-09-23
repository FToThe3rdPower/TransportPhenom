#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ex1_equations as ex1

R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
U = 100e-3    #m/s
mu = 0.001 #Pa s
r = np.linspace(R1, R2, 100) #Distance tube (region of interest)
r_mm = np.linspace(R1*1e3, R2*1e3, 100)
Qw_ = 2.2 # To make a better legend hihi
Qw = (Qw_/60)*1e-6 #Qw in SI-units
w1 = (1000/60) * 2 * np.pi # rad/s
w2 = (3000/60) * 2 * np.pi # rad/s


##Velocity profile
plt.figure()
ex1.vel_plot_2(r, R1, R2, U, mu, Qw, Qw_, r_mm, w1, w2)

df = pd.read_csv('COMSOL_velocity.csv')
x = []
y = []
for i in range(len(df)):
    x.append(df.iloc[i][3])
    y.append((df.iloc[i][4]))

plt.scatter(x, y, label="COMSOL simulation", color="orange", marker=".")
plt.legend()

##Shear stress
plt.figure()

df = pd.read_csv('COMSOL_velocity.csv')
x = []
y = []
for i in range(len(df)):
    x.append(df.iloc[i][6])
    y.append((df.iloc[i][7])*(2*np.pi)) #Conversion to rad/s cause forgot in COMSOL

plt.scatter(x, y, marker=".", label="COMSOL simulation", color="orange")
ex1.stress_plot_2(r, R1, R2, U, mu, Qw, Qw_, r_mm, w1, w2)


plt.legend()
plt.show()