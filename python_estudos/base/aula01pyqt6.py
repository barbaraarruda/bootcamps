#created by @barbara 11:10 2022.08.25

import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(300,300) #500 de largura, 400 de altura
janela.setWindowTitle("Primeira")
janela.show()


app.exec()
