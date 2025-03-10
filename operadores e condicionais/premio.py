P = int(input())
D = int(input())
B = int(input())

pontuacao = (1 * P) + (2 * D) + (3 * B)

if pontuacao >= 150:
    print("B")

elif pontuacao >= 120:
    print("D")

elif pontuacao >= 100:
    print("P")

else:
    print("N")