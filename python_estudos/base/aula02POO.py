#created by @barbara 2022.08.16 14:52

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade): #self referencia a instância
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): #esses outros métodos são específicos para cada objeto, cada objeto terá um valor diferente. 
        print(self.ano_atual - self.idade)

    @classmethod #refere a classe em geral #este é um método decorador <<novidade>>
    def por_ano_nascimento(cls, nome, ano_nascimento):  #aqui não se utiliza o self, utiliza o cls ou qualquer outra para se referenciar a classe. Não pode usar a palavra reservada class.
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
