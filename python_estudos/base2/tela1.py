import PySimpleGUI as sg


class TelaLogon:
    def __init__(self):
        # Layout
        layout = [

            [sg.Text('Usuário:  ', size=(10,0)), sg.Input(size=(15,0))],
            [sg.Text('Senha: ', size=(10,0)), sg.Input(size=(15,0))],
            [sg.Button('Entrar'), sg.Button('Sair')]

        ]

    # janela

        tela1 = sg.Window("Tela de Logon").layout(layout)

    # extrair os dados da tela

        self.button, self.values = tela1.read()

    def start(self):
        print(self.values)


tela2 = TelaLogon()
tela2.start()
