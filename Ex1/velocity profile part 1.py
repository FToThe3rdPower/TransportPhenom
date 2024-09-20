import numpy as np
import matplotlib.pyplot as plt



def trth(R1, R2, w1,w2,r,mu):
	trth =(2*mu*(R1^2)*(R2^2)*(w1-w2))/(((R2^2)-(R1^2))*(r^2))
	return trth


R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
mu = 0.001 #Pa s
w1 = 314.15 #rad/s
w2 = 104.71 #rad/s

r = np.linspace(R1, R2, 100)



plt.plot(r, trth(r, R1, R2, w1, w2,mu))
plt.show()
