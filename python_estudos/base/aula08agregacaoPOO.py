#created by @barbara 2022.08.16 22:10
"""
agregação e composição são relação de todo parte. Onde uma classe usa outra classe como parte de si e essa classe precisa da outra classe.
"""

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())

#----------------------------------------------------------------------------------------------------------------------------- (classes.py)

#created by @barbara 2022.08.16 22:10

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
