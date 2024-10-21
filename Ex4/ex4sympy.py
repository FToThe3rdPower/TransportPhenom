#!/usr/bin/python3

import sympy as sp
import numpy as np
from sympy import *

#sympy setup
##symbol declaration
y, t, D, R = symbols("y t D R")

#Concentration function we actually care about
c = Function("c")

#helper funcs
Φ,Θ = map(Function, "φθ")

#define our PDE
pdeq = Eq(c(y,t).diff(t), -D * c(y,t).diff(y,y) + R)



#Actually execute PDE solver
print( pde_separate(pdeq, c(y,t), [Φ(y), Θ(t)], strategy="add") )

#answer
'''[Derivative(φ(y), (y, 2)) - R/D, -Derivative(θ(t), t)/D]'''