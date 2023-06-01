#created by @barbara 2022.08.16 16:56

class A:
    vc = 123 #variável de classe, disponível para todas as instâncias

    def __init__(self):
        pass



a1 = A()
a2 = A()

A.vc = 'Alterado'
#a1.vc = 321 #criou um atributo direto na instância, não alterou o valor na classe.



print()


print(a1.vc)
print(a2.vc)
print(A.vc)
