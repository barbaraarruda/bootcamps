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
