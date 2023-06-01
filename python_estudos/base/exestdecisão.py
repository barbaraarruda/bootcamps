"""
created on 2022.05.13 @barbara
"""

def linha():
    print("-----------------------------")

print("Bem vindo!")
linha()
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
linha()
media = (n1 + n2)/2

if media > 6:
    print("Aluno aprovado! Média final:",media)
elif media > 4 < 6:
    print("Aluno em exame. Média final: ",media)
else:
    print("ALuno reprovado.", media)
