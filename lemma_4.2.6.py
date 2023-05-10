import math
import itertools
import numpy as np

MA = np.matrix([[1,0,2],[-1,0,2],[0,1,0]])                                  # matrix MA
MB = np.matrix([[0,1,0],[0,-1,0],[1,0,0]])                                  # matrix MB
ell = 1.658967                                                              # a value smaller than λ

MA_exponents = range(1,26)                                                  # α ranges from 1 to 26, inclusive
MB_exponents = range(1,3)                                                   # β ranges from 1 to 2, inclusive

for a, b in itertools.product(MA_exponents, MB_exponents):                  # a = α, b = β
    prod = np.linalg.matrix_power(MA, a)                                    # MA^α
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b))                   # MA^α * MB^β
    norm = np.linalg.norm(prod, 2)/(ell**(a + b))                           # || (MA^α * MB^β)/l^(α + β) ||
    if norm > 1:                                                            # prints α, β, and norm if norm is greater than 1
        print(f"alpha = {a} | beta = {b} | norm = {norm}")