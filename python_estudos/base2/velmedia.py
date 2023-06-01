#faça um programa de velocidade média

distancia = float(input("digite a distância percorrida: "))
print()

unidade = input("Digite a unidade de velocidade: ")
print()

tempo = float(input("Digite o tempo de deslocamento: "))
print()

vel_media = (distancia / tempo)
print(f"A velocidade média para o deslocamento de {distancia} {unidade} e tempo {tempo} é {vel_media} {unidade}/h")
