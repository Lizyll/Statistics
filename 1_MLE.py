import sympy as sym
import numpy as np
from scipy.special import comb

# define the likelihood function
def Likelihood(n, x, p):
	former = comb(n, x)
	later = pow(p, x) * pow((1-p), n-x)
	return former * later

# the log likelihood function
def logL(n, x, p):
	return np.log(Likelihood(n,x,p))

# the derivative of the log likelihood
def dL(n, x, p):
	return (x * 1/p) + ((x-n)/(1-p))

sym.init_printing(use_unicode=False, wrap_line=True)
p = sym.Symbol('p')
print(sym.solveset(dL(10,8,p), p)) 
