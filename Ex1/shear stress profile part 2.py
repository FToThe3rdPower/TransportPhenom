import numpy as np
import matplotlib.pyplot as plt



def tth(r, R1, R2, w1,w2,mu):
	
	t_th = (2*mu*(R1**2)*(R2**2)*(w2-w1))/(((R2**2)-(R1**2))*(r**2))
 
	return t_th


R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
w1 = 18840      #rad/s
w2 = 6280     #rad/s
mu = 0.001 #Pa s


r = np.linspace(R1, R2, 100)



plt.plot(r, tth(r, R1, R2,w1, w2 , mu))
plt.show()