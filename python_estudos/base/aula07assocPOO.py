#created by @barbara 2022.08.16 21:48

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property #getter
    def nome(self):
        return self.__nome

    @property #getter
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')
        
        
        
#main ----------------------------------------------------------------------------------------------

#created by @barbara 2022.08.16 21:48
"""
trata sobre associação, onde uma classe estará associada a outra classe, mas nenhuma das duas classes dependem uma da outra. Ambas as classes
podem viver uma sem a outra.
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
