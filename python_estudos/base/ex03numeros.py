"""
created on 2022-11-05 @barbara
"""
#escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 35%.

print("Bem vindo!")


def linha():
    print("_________________________________")


linha()
salario = float(input("Digite o salário do funcionário: "))
reajuste = salario * (35 / 100)
novo_salario = salario + reajuste
linha()
print("O novo salário com reajuste é: ", novo_salario)
