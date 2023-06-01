# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:36:52 2021

@author: barbara

lista de exercícios
"""

#01. Crie 10 variáveis, atribua conteúdos diversos, imprima o conteúdo e o tipo de cada uma, faça casting para outro tipo. 

var1 = input("Digite um número: ")
var1 = int(var1)
print(type(var1))
print("*************************")
print()
var2 = input("Digite um número com ponto flutuante: ")
var2 = float(var2)
print(type(var2))
print("*************************")
print()
var3 = input("Digite uma palavra: ")
print(type(var3))
print("*************************")
print()
var4 = input("Qual sua cor favorita? ")
print(type(var4))
print("*************************")
print()
var5 = input("Digite quantos carros sua família possui: ")
var5 = int(var5)
print(type(var5))
print("*************************")
print()
var6 = input("Digite o valor arrendondado de π: ")
var6 = float(var6)
print(type(var6))
print("*************************")
print()
var7 = input("Quantos bombons você consegue comer em 3 minutos? ")
var7 = int(var7)
print(type(var7))
print("*************************")
print()
var8 = input("Qual é o seu IMC? ")
var8 = float(var8)
print(type(var8))
print("*************************")
print()
var9 = input("Você gosta de abacate? ")
print(type(var9))
print("*************************")
print()
var10 = input("Digite um modelo de avião que você gostaria de comprar: ")
print(type(var10))


# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:21:41 2021

@author: barbara

lista de exercícios
"""
#02 Faça um programa que calcule a área de uma figura geométrica de sua escolha, depois exiba uma mensagem amigável informando o nome da figura e sua área em metros quadrados. 
#adaptado 

print("Vamos calcular a área de uma figura geométrica!")
print()
print("-----------------------------------------------")
print("Escolha uma dessas figuras geométricas:")
print("Triângulo; Quadrado; Losango;")
print("Retângulo, Trapézio, Círculo")
print()
figura = input("Digite a figura desejada: ")
print("A figura escolhida foi: ",figura)
print("-----------------------------------------------")

if (figura == "Triângulo"):
    areatri = float(input("Digite a área: "))
    basetri = float(input("Digite a base: "))
    alturatri = float(input("Digite a altura: "))
    
    resfintri = (basetri * alturatri)/2
    print("O resultado da área em m² do triângulo é:  ",resfintri)

if (figura == "Quadrado"):
    ladoqua = float(input("Digite o lado: "))
    
    resfinqua = ladoqua * ladoqua
    print("O resultado da área em m² do quadrado é: ",resfinqua)
    
if (figura == "Losango"):
    diagmen = float(input("Digite a diagonal menor: "))
    diagmai = float(input("Digite a diagonal maior: "))
    
    resfinlos = (diagmen * diagmai)/2
    print("O resultado da área em m² do losango é:  ",resfinlos)
    
if (figura == "Retângulo"):
    baseret = float(input("Digite a base do retângulo: "))
    alturaret = float(input("Digite a altura do retângulo: "))
    
    resfinret = (baseret * alturaret)
    print("O resultado da área em m² do retângulo é:  ",resfinret)
    
if (figura == "Trapézio"):
    basemitrap = float(input("Digite a base maior do trapézio: "))
    basemntrap = float(input("Digite a base menor do trapézio: "))
    alturatrap = float(input("Digite a altura do trapézio: "))
    
    resfintrap = ((basemitrap + basemntrap) * alturatrap)/2
    print("O resultado da área em m² do trapézio é: ",resfintrap)
    
if (figura == "Círculo"):
    print("Atenção: aqui será utilizado o valor aproximado da constante de Pi informada pelo usuário")
    raiocir = float(input("Digite o raio do círculo: "))
    constpi = float(input("Digite o valor da constante de pi considerada para o cálculo: "))
  
    
    resfincir = constpi * (raiocir * raiocir)
    print("O resultado da área em m² do círculo é:  ",resfincir)
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:24:43 2021

@author: barbara

lista de exercícios
"""
#03 - Fazer uma operação matemática e exibir os dados:
    
print("**************************************************")
print("Esse programa irá realizar uma operação matemática")
print("**************************************************")
print()

print("As operações que são aceitas:")
print()
operacoes = ["+", "-","x", "/"]
print(operacoes)
print()
print("_________________________________________________")

escolhaop = input("Digite o símbolo da operação desejada: ")
print()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("_________________________________________________")
print ("Os números escolhidos foram:")
print(num1)
print(num2)
print()
print("_________________________________________________")

if (escolhaop == "+"):
    resadic = num1 + num2
    print("O resultado da adição é: ",resadic)
    
elif (escolhaop == "-"):
    ressub = num1 - num2
    print("O resultado da subtração é: ",ressub)

elif (escolhaop == "x"):
    resmul = num1 * num2
    print("O resultado da multiplicação é: ",resmul)

else:
    resdiv = num1 / num2
    print("O resultado da divisão é: ",resdiv)
