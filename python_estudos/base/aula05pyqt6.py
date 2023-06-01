#created by @barbara 11:10 2022.08.25

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1():
    #print("teste") #este comando sai teste no interpretador.
    label.setText("Botão 1 pressionado!")
    label.adjustSize()

def funcao2():
    label.setText("Botão 2 pressionado!")
    label.adjustSize()

def funcao3():
    valor_lido = le.text()
    label.setText(valor_lido)
    label.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800,600) #500 de largura, 400 de altura
janela.setWindowTitle("Primeira")

btn = QPushButton("Botão 1", janela)
btn.setGeometry(100,100,150,80)
btn.setStyleSheet('background-color: pink; color: black')
btn.clicked.connect(funcao1)

btn2 = QPushButton("Botão 2", janela)
btn2.setGeometry(100,200,150,80)
btn2.setStyleSheet('background-color: silver; color: black')
btn2.clicked.connect(funcao2)

btn3 = QPushButton("Botão 3", janela)
btn3.setGeometry(100,300,150,80)
btn3.setStyleSheet('background-color: blue; color: black')
btn3.clicked.connect(funcao3)

label = QLabel("Texto", janela)
label.move(400, 100)
label.setStyleSheet('font-size:30px')

le = QLineEdit("", janela)
le.setGeometry(500, 200, 150, 40)

janela.show()


app.exec()
