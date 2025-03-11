N = int(input()) #o número de pessoas infectadas no dia 0
R = int(input()) # fator reprodutivo da infecção
P = int(input()) #número alvo de pessoas infectadas

dias = 0
t_infectados = N
n_infectados = N

while t_infectados < P:
    n_infectados *= R
    t_infectados += n_infectados
    dias += 1


print(dias)    