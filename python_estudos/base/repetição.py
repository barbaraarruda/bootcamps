"""
created on 2022.14.05 11:19 @barbara
"""
def linha():
    print("______________________________")

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor:  "))
opção = 0

linha()
while opção !=5:
    print("[1] somar"
          "\t\n[2] multiplicar"
          "\t\n[3] maior"
          "\t\n[4] novos números"
          "\t\n[5] sair do programa")
    opção = int(input("Digite a opção desejada: "))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} resultou em {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'A multiplicação de {n1} por {n2} resultou em {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")
    linha()
print("Fim do programa! Volte sempre!")
