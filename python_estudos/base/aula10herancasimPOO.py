#created by @barbara on 2022.08.18 11:16
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

from classes import *  #esse comando importa tudo que estiver no arquivo. Os outros, importam apenas objetos específicos. Recomenda-se que tenha importação apenas do que seja preciso e não do geral.

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()


a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()
print(p1.idade)

#---------------------------------------------------------------------------------------------------------------(classes.py)

#created by @barbara on 2022.08.18 11:16

class Pessoa:    #essa classe é chamada de superclasse #essa classe não herdou nada das outras.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa): #essas classes são chamadas de subclasses #é uma melhoria da superclasse, é uma especificidade.
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self): #método
        print(f'{self.nomeclasse} estudando...')
