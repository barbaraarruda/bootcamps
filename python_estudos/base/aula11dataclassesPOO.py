#created by @barbara 18:37 2022.08.22

"""
dataclasses usar para dados.
"""

from dataclasses import dataclass,field

class OLdPerson:
    def __init__(self, name, lastname):
        self.name = name           #aqui é campo de instância.
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name}' \
         f'({self.name} {self.lastname})'
        return class_str

    def __repr__(self):
        return str(self)

    def __eq__(self, o: object):
        return self.lastname == o.lastname

@dataclass(
    frozen=True, slots=True
)
class Person:
    name: str                #aqui parece ser campo de classe mas não é, é campo de instância.
    lastname: str
    active: bool = False
    addresses: list = field(
        default_factory=list, repr=False, compare=True

        #compare vai comparar os dados. Por exemplo, se estiver com valor true, ele compara. Se estiver com valor False, ele não vai comparar esse campo, apenas os outros que estiver ativo.
        #kw_only se refere a keyword only. Significa que você apenas quer valores referentes a palavras aqui.
    ) #default factory é um executável
    full_name: str = field(
        default='Missing', init=False, repr=False   #o init é quando você inicia os valores dessa classe, não é um construtor no caso.
    ) #default aqui é um padrão

    def __post_init__(self): #pode usar o post init para inicializar coisas dentro do objeto #aqui é uma gambiarra para inicializar, pois como padrão não tem como - tornou dinâmico.
        full_name = f'{self.name}' \
            + ' ' + f'{self.lastname}'
        object.__setattr__(
            self,
            'full_name', full_name
        )
    
    def get_full_name(self):
        return self.full_name
        

if __name__ == '__main__' :
    john1 = Person(
        'John', 'Doe', True, ['R1']
    )
    john2 = Person(
        'John', 'Doe', True, ['R2']
                   )
    #john1.active = True  #posso usar esse comando ou o que está dentro da instância.
    print(john1)
    print(john2.full_name)
    print(john1 == john2)
