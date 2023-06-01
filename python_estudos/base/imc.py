#calculadora de IMC - exc prova

def linha():
    print("_____________________________")

print("Bem vindo!")
linha()
print("Calculadora de IMC")
print("Esse programa irá calcular o seu índice de massa corporal")
linha()
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

calcimc = (peso/(altura**2))

linha()

if calcimc <= 18.5:
    print(f'Você está abaixo do peso. Seu IMC é {calcimc}')
elif calcimc <= 24.9:
    print(f'Você está saudável. Seu IMC é {calcimc}')
elif calcimc <= 29.9:
    print(f'Você está com peso em excesso. Seu IMC é {calcimc}')
elif calcimc <= 34.9:
    print(f'Você está com obesidade grau I. Seu IMC é {calcimc}')
elif calcimc <= 39.9:
    print(f'Você está com obesidade grau II; Seu IMC é {calcimc}')
else:
    print(f'Você está com obesidade grau III. Seu IMC é {calcimc}')
