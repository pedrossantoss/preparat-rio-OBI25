N = int(input())

lista = 0

for i in range(N):
    A = int(input())
    lista += A
    if lista >= 1_000_000:
        print(i + 1)
        break