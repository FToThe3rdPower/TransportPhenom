import numpy as np
import matplotlib.pyplot as plt



def uth(r, R1, R2, w1,w2):
	
	u_th = ((R2**2)/((R2**2)-(R1**2)))*((w2-((w1*(R1**2))/(R2**2)))*r-(((w2-w1)*(R1**2))/r))
 
	return u_th


R1 = 0.1e-3   #m
R2 = 0.4e-3   #m
w1 = 18840      #rad/s
w2 = 6280    #rad/s


r = np.linspace(R1, R2, 100)



plt.plot(r, uth(r, R1, R2,w1, w2))
plt.show()