X = int(input())
N = int(input())

quota = X

for i in range(N):
    Mi = int(input())
    quota = quota - Mi + X

print(quota)