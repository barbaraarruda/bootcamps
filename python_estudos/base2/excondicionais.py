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
    
    

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:14:20 2021

@author: barbara
"""
#Faça um programa em python que pergunte seu nome, sua idade e tenha classificação de acordo com a sua idade.

nome = (input("Insira o nome do usuário: "))
idade = int(input("Insira a idade do usuário: "))
print("_________________________________")

if (idade >= 0) and (idade <= 14):
    print("O usuário é uma criança.")
if (idade >= 15) and (idade <= 17):
    print("O usuário é um adolescente.")
if (idade >= 18) and (idade <= 60):
    print("O usuário é um adulto.")
else:
    print("O usuário é um idoso.")
    
    
 
