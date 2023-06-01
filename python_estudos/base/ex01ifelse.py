"""
created on 2022-11-05 21:18 @barbara
"""
def linha():  #faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).
    print("----------------------------")

print("Bem vindo!")

linha()


n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1 + n2)/2

linha()

if media < 6:
    print("A média do aluno é:", media, ",está reprovado.")
else:
    print("A média do aluno é:", media, ",está aprovado.")
