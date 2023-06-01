"""
created on 2022.05.13 @barbara
"""

def linha():
    print("______________________________")

print("Bem vindo!")
linha()
print("Esse programa irá calcular uma progressão aritmética")
linha()

S = 0
for x in range (3,333,3):    #range(i,n, p) > gera um intervalo de i a n-1 com intervalo p entre os números.
    S = S + x
print("O resultado da PA é:",S)
