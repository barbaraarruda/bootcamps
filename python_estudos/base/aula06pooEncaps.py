#created by @barbara 2022.08.16 17:08
"""
public, protected, private
public são métodos e atributos que podem ser acessados dentro e fora da classe.
protected são atributos que podem ser acessados apenas dentro das classes ou das filhas dessa classe.
private o método e o atributo só está disponível dentro daquela classe.
...
Em python, não faz sentido para os desenvolvedores da linguagem usar esses parâmetros. Por isso, eles não incluíram tais palavras. Em python, temos:
_ >> private, de maneira fraca, sutil. Você consegue acessar. Em outras linguagens, ele seria o PROTECTED. Recomenda que não seja acessado. (public _)
__ >> private, de maneira FORTE, proíbe o acesso ao atributo/método. De maneira alguma, ele deve ser acessado. (_NOMECLASSE__nomeatributo) <pode acessar e modificar ele fora da classe dessa forma.

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Rose')


print(bd.dados)
