import math

for i in range(1, 100):
    lhs = 100*i**2 
    rhs = 2**i 
    
    if lhs < rhs:
        print(f'n이 {i}일 때 => True')
    elif lhs > rhs:
        break
