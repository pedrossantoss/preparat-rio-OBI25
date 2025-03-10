N = int(input())
P = int(input())

bact = 1
dias = 0

while bact * P <= N:
    bact *= P
    dias += 1

print(dias)