import PySimpleGUI as sg


class TelaInicial:
    def __init__(self):
        layoutinicial = [
            [sg.Text('Usuário'), sg.Input(), sg.Input()],
            [sg.Input(), sg.Input(), sg.Input(), sg.Button('Buscar')],
            [sg.Combo('Texto'),],
            [sg.Button('Salvar'), sg.Button(), sg.Button()]
        ]

        telainicial1 = sg.Window("Agenda de Contatos").layout(layoutinicial)

        self.button, self.values = telainicial1.read()

    def start(self):
        print(self.values)

telainicial2 = TelaInicial()
telainicial2.start()
