#created by @barbara 2022.08.22 22:46
"""
Classes são moldes para criar novos objetos. Classes criam instâncias delas mesmas.
Instância é um objeto gerado pela classe. Ex.: massa de bolo para cookie. Temos a massa de bolo do cookie (classe), temos as forminhas.
Dentro das classes, são 'setadas' as configurações (forminhas). Toda vez que usamos o self, estamos falando da instância da classe, estamos falando do objeto. No exemplo dado,
estaríamos falando dos cookies em si, não estamos falando exatamente da classe.
Tudo é um objeto em Python. Não só as instãncias, como a classe em si é objeto.
Uma instância de uma classe é um tipo criado por você!
Type não é uma função, é uma classe.
__init__ é o método que inicializa os valores dos atributos de instância.
Metaclasses são classes que criam novas classes (elas herdam de type). Não é comum usar metaclasses. Apenas em casos muito específicos.
Sempre utilize o módulo abc para classes abstratas em Python.
"""

class NameMyMetaClass(type): #toda classe que herda de type é uma metaclasse.
    def __new__(mcs, name, bases, namespace): #esse método new é utilizado para criar novos objetos. Ele é utilizado antes do init. 
        print('__new__ da metaclass')

        if name == 'Person':
            raise Exception('Cannot use name Person')

        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class Person(metaclass=NameMyMetaClass):
    def __new__(cls, *args, **kwargs): #a diferença do new para o init é: o new cria os objetos, o init inicializa esses objetos.
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self, name, lastname):
      print('__init__ da class')
      self.name = name #seta = configura. #self == instância
      self.lastname = lastname

#def init_person(self, name, lastname):
#    self.name = name #seta = configura. #self == instância
#   self.lastname = lastname

#Person = type('Person', (), {
#    '__init__': init_person
#
#})



person1 = Person('Luiz', 'Otávio')
person2 = Person('Maria', 'Oliveira')
#print(type(person1))
print(type(Person)) #a classe em si é do tipo type
print(person1.name)
print(person2.name)
