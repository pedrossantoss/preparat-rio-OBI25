N = int(input())
N2 = list(map(int, input().split()))

A = 0
B = 0

for i in range(N2.count(1)):
    if A == 0:
        A = 1
    else:
        A = 0    

for i in range(N2.count(2)):
    if B == 0:
        B = 1
    else:
        B = 0       
    if A == 0:
        A = 1
    else:
        A = 0      

print(A)
print(B)