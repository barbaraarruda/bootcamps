"""
created on 2022-11-05 19:58 @barbara
"""
#escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

z = (num1**2 + num2**2)/(num1 - num2)**2

print("O valor de z é: ", z)
