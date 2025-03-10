X = int(input())
Y = int(input())

def preco_ing(idade):
    if idade <= 17:
        return 15
    elif 18 <= idade <= 59:
        return 30
    else:
        return 20
    
ingresso = preco_ing(X) + preco_ing(Y)

print(ingresso)