D = int(input())  
A = int(input())  
N = int(input())  

dias = 32 - N  


if N <= 15:
    diaria = D + (N - 1) * A
else:
    diaria = D + 14 * A 


estadia = dias * diaria

print(estadia)
