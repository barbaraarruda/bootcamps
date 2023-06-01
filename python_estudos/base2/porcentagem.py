#calcular porcentagem

valor = float(input("Digite um valor: "))

percentual = float(input("Qual porcentagem deseja calcular? "))

#porcentagem = valor * (valor_percentual / 100)

result_porcentagem = (valor * (percentual / 100))

print(f"A porcentagem {percentual}% do valor {valor} é {result_porcentagem}.")  #o uso de { } junto com o f é uma alternativa para concatenar
