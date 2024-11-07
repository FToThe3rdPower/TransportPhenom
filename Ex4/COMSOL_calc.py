import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "D:/Documents/Transport Phenomena/TransportPhenom/Ex4/COMSOL_plot.xlsx"
df = pd.read_excel(file)

r = df["R"]
c1 = df["c1"]
c2 = df["c2"]
L = 0.01/2
kA = 2
kB = 0.5
Deff = 1.18e-6


rateB = 0
rateC = 0
for i in range(len(r)):
	rateB += (kA*c1[i]) - (kB*c2[i])
	rateC += kB*c2[i]

selectivity = rateC/rateB


print(f"The selectivity value is {selectivity}")

