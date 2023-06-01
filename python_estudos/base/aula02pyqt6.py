#created by @barbara 11:10 2022.08.25

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800,600) #500 de largura, 400 de altura
janela.setWindowTitle("Primeira")

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100,100,150,80)
btn.setStyleSheet('background-color: pink; color: black')

label = QLabel("Texto", janela)
label.move(400, 100)

janela.show()


app.exec()
