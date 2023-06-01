# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:36:30 2021
 
@author: barbara
"""
#calculadora de raiz quadrada
#utiliza-se aqui potência fracionária para resolução de problemas sem a necessidade de importar bibliotecas
 
print("Calculadora de raiz quadrada")
print("____________________________")
print()
 
num1 = float(input("Digite o radicando da raiz: "))
num2 = float(input("Digite o índice da raiz: "))
num3 = float(input("Digite o expoente da raiz: "))
print()
 
res = float(num1**(num3/num2))
print("__________________________")
print ("O resultado é: ",res)
