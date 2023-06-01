#created by @barbara 2022.08.16 15:09

from random import randint

class Pessoa: #classe é um molde para gerar novos objetos
    ano_atual = 2022

    def __init__(self, nome, idade): #self referencia a instância
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): #esses outros métodos são específicos para cada objeto, cada objeto terá um valor diferente.
        print(self.ano_atual - self.idade)

    @classmethod #refere a classe em geral #este é um método decorador <<novidade>> #método de instância.
    def por_ano_nascimento(cls, nome, ano_nascimento):  #aqui não se utiliza o self, utiliza o cls ou qualquer outra para se referenciar a classe. Não pode usar a palavra reservada class.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod #não precisa nem da classe, nem da instância. É "uma função normal", mas por organização precisa estar dentro da classe. Não recebe nem a classe nem a instância (não precisa, apenas se quiser).
    def gera_id(): #não pode usar nem cls nem self aqui dentro.
        rand = randint(10000, 19999) #essa variável só funciona dentro do método estático.
        return rand



#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())
