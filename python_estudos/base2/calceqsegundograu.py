# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:23:41 2021

@author: barbara
"""

#extrair as raízes de equação do segundo grau.
#esta parte da calculadora foi escrita por mim //barbara.arruda// para auxiliar o aprendizado de matemática.

print("#Calculando Equações de Segundo Grau#")
print("Instruções para utilizar o programa:")
print("__________________________________________")
print("Equação do segundo grau utiliza o formato:")
print(" ax² + bx + c = 0, com a diferente de 0.")
print("a representa o coeficiente de x²;")
print("b representa o coeficiente de x;")
print("c representa o termo independente.")
print("__________________________________________")
print()

eqa = float(input("Digite o coeficiente de x²: "))
eqb = float(input("Digite o coeficiente de x: "))
eqc = float(input("Digite o termo independente: "))
print()

print("__________________________________________")
print("Primeira etapa: cálculo do delta.")
delta = (eqb**2 - 4 * eqa * eqc)
print("O delta da equação é: ",delta)
print()
print("Atenção:")
print("a.Se delta > 0, há duas raízes reais e diferentes.")
print("b.Se delta < 0, não existe raíz real.")
print("c.Se delta=0, existem duas raízes reais e iguais.")
print()

print("__________________________________________")
print("Segunda etapa: extração das raízes.")
raiz1 = (-eqb + delta**(1/2)) / (2*eqa)
raiz2 = (-eqb - delta**(1/2)) / (2*eqa)
print("O resultado das raízes são:")
print("Raíz 1: ",raiz1)
print("Raíz 2: ",raiz2)
print()
print("Cálculo finalizado.")




# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:28:27 2021

exemplos códigos estruturas condicionais

@author: barbara
"""
#Faça um programa em python que pergunte seu nome e idade, imprima sua idade e nome e se você for maior de idade, imprima uma mensagem e se não for, imprima outra mensagem 

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
print("______________________")

print(f"O nome inserido do usuário é {nome} e sua idade é {idade}")



if idade >= 18: 
    print("O usuário é maior de idade.")
elif idade < 18:
    print("O usuário é menor de idade.")
