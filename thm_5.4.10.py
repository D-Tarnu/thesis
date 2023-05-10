import math
import itertools
import numpy as np

MA = np.matrix([[1,0,2],[-1,0,2],[0,1,0]])
MB = np.matrix([[0,1,0],[0,-1,0],[1,0,0]])
ell = 1.658967

### checking exceptions to (5.38)

print("Exceptions to (5.39):")

MA_exponents = range(1,35)
MB_exponents = range(1,3)

exceptions = False                                                              

for a1, b1, a2, b2 in itertools.product(MA_exponents, MB_exponents, MA_exponents, MB_exponents):                # a1 = α_1, b1 = β_1, a2 = α_2, b2 = β_2
    prod = np.linalg.matrix_power(MA, a2)                                    
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b2))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, a1))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b1))                    
    norm = np.linalg.norm(prod, np.inf)/(ell**(a1 + b1 + a2 + b2))                                                           
    if norm > 1.093:                                                                                            
        exceptions = True

if not exceptions:
    print("No exceptions")

print("\n")

### checking exceptions to (5.40)

print("Exceptions to (5.40):")

MA_exponents = range(1,10)
MB_exponents = range(1,3)

for a1, b1, a2, b2 in itertools.product(MA_exponents, MB_exponents, MA_exponents, MB_exponents):               
    prod = np.linalg.matrix_power(MA, a2)                                    
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b2))
    prod = np.matmul(prod, np.linalg.matrix_power(MA, a1))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b1))                    
    norm = np.linalg.norm(prod, np.inf)/(ell**(a1 + b1 + a2 + b2))                                               
    if norm > 0.9148:                                                                                            
        print(f"alpha_1 = {a1} | beta_1 = {b1} | alpha_2 = {a2} | beta_2 = {b2} | norm = {norm}")

print("\n")

### checking exceptions to (5.41)

print("Exceptions to (5.41):")

MA_exponents = range(1,5)
MB_exponents = range(1,3)

exceptions = False                                                              

for a1, b1, a2, b2, a3, b3, a4, b4 in itertools.product(MA_exponents, MB_exponents, MA_exponents, MB_exponents, MA_exponents, MB_exponents, MA_exponents, MB_exponents):                
    prod = np.linalg.matrix_power(MA, a4)                                    
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b4))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, a3))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b3))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, a2))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b2))  
    prod = np.matmul(prod, np.linalg.matrix_power(MB, a1))
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b1))                    
    norm = np.linalg.norm(prod, np.inf)/(ell**(a1 + b1 + a2 + b2 + a3 + b3 + a4 + b4))                                                           
    if norm > 1:                                                                                            
        exceptions = True

if not exceptions:
    print("No exceptions")

print("\n")

### checking exceptions to (5.42) and (5.44)

print("Potential exceptions to (5.42)/(5.44):")

MA_exponents = range(1,51)
MB_exponents = range(1,3)

for a, b in itertools.product(MA_exponents, MB_exponents):                  
    prod = np.linalg.matrix_power(MA, a)                                    
    prod = np.matmul(prod, np.linalg.matrix_power(MB, b))                   
    norm = np.linalg.norm(prod, np.inf)/(ell**(a + b))                      
    if norm > 0.8:                                                        
        print(f"alpha = {a} | beta = {b} | norm = {norm}")

print("\n")