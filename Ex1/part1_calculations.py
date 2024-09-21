import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ex1_equations as ex1

R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
U = 100e-3    #m/s
mu = 0.001 #Pa s

Qw_ = [1.0, 1.5, 2.2] # To make a better legend hihi
Qw = [] #Qw in SI-units
for i in range(len(Qw_)):
	Qw.append((Qw_[i]/60)*1e-6) #m^3/s


r = np.linspace(R1, R2, 100) #Distance tube (region of interest)
r_mm = np.linspace(R1*1e3, R2*1e3, 100)
#Velocity plots
plt.figure()
for i in range(len(Qw)):
	ex1.vel_plot_1(r, R1, R2, U, mu, Qw[i], Qw_[i], r_mm)

#Shear stress plot
plt.figure()
for i in range(len(Qw)):
	ex1.stress_plot_1(r, R1, R2, U, mu, Qw[i], Qw_[i], r_mm)

plt.show()


#COMSOL simulation
df = pd.read_csv('2_veldata.csv')
x = []
y = []
for i in range(len(df)):
    x.append(df.iloc[i][0])
    y.append((df.iloc[i][1]))



ex1.vel_plot_1(r, R1, R2, U, mu, Qw[2], Qw_[2], r_mm) ##Only 2.2 ml/min
plt.scatter(x, y, label="COMSOL simulation", marker=".")
plt.legend()
plt.show()


