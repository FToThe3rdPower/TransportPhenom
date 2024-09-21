import numpy as np
import matplotlib.pyplot as plt



def tr(r, R1, R2, U, mu, Qw):
	J = ((((R1**4)/4) - ((R2**4)/4)) * np.log(R2/R1)) + (((R2**2)/2)  - ((R1**2)/2))**2
	dpdz = ((2*mu*np.log(R2/R1))/(np.pi*J)) * (Qw + (((2*np.pi*U)/np.log(R1/R2))* ( (((R1**2)/2)*np.log(R1/R2)) + ((R2**2)/4) - ((R1**2)/4) )) )
	t_z = -(dpdz*(r/2))+(U+dpdz*((R2**2)-(R1**2))/(4*mu))*(mu/(np.log(R2/R1)*r))
 
	return t_z


R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
U = 100e-3    #m/s
mu = 0.001 #Pa s
Qw = (2.2/60)*1e-6    #m3/s 

r = np.linspace(R1, R2, 100)



plt.plot(r, tr(r, R1, R2, U, mu, Qw))
plt.show()