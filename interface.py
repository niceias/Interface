import sys
import PyQt5.QtWidgets as qtw #biblioteca de labels
import PyQt5.QtGui as qtg #biblioteca de fontes
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui #trabalha com imagens


class App(qtw.QWidget):
    def __init__(self):
        super().__init__()
       #TODO: CONFIG DA JANELA
        self.topo = 100
        self.esquerda = 320
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela!!"

       #TODO: CAIXA DE TEXTO
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(50,20)
        self.caixa_texto.resize(250,20)

      #TODO: CRIAÇÃO DE BOTÕES
        self.botao_a = qtw.QPushButton('Botão 1', self)
        self.botao_a.move(80, 100)
        self.botao_a.resize(100, 40)
        self.botao_a.setStyleSheet('QPushButton {background-color: #ADD8E6;'
                              'font: bold 12px;'
                              'border-style: outset;'
                              'border-widht: 10px;'
                              'border-color: black}')
        self.botao_a.clicked.connect(self.botao_clicka)

        self.botao_texto = qtw.QPushButton('Texto', self)
        self.botao_texto.move(310, 20)
        self.botao_texto.resize(50, 20)
        self.botao_texto.setStyleSheet('QPushButton {background-color: orange;'
                                   'font: bold 12px;'
                                   'border-style: outset;'
                                   'border-widht: 10px;'
                                   'border-color: black}')
        self.botao_texto.clicked.connect(self.mostra_texto)

        botao_b = qtw.QPushButton('Botão 2', self)
        botao_b.move(200, 100)
        botao_b.resize(100, 40)
        botao_b.setStyleSheet('QPushButton {background-color: #98FB98;'
                              'font: bold 12px;'
                              'border-style: outset;'
                              'border-widht: 10px;'
                              'border-color: black}')
        botao_b.clicked.connect(self.botao_clickb)

        # TODO: CRIAÇÃO DE LABEL
        self.label_a = QLabel(self)
        self.label_a.setText('Aperte algum botão')
        self.label_a.move(50, 50)
        self.label_a.resize(300, 50)
        self.label_a.setStyleSheet('QLabel {font: bold 25px;''color: blue}')

        self.label_texto = QLabel(self)
        self.label_texto.setText('Você Digitou: ')
        self.label_texto.move(450, 50)
        self.label_texto.resize(300, 50)
        self.label_texto.setStyleSheet('QLabel {font: bold 15px;''color: black}')


        #LABEL DO CARRO
        self.carro_1 = QLabel(self)
        self.carro_1.move(100,180)
        self.carro_1.resize(800,400)


        self.carregar_janela()

    #TODO: FUNÇOES
    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)

        self.show()

    def botao_clicka(self):
        self.label_a.setText("O Botão 1 foi clicado")
        self.label_a.setStyleSheet('QLabel {font: bold 25px;''color: green}')
        self.carro_1.setPixmap(QtGui.QPixmap('senna.png'))

    def botao_clickb(self):
        self.label_a.setText("O Botão 2 foi clicado")
        self.label_a.setStyleSheet('QLabel {font: bold 25px;''color: red}')
        self.carro_1.setPixmap(QtGui.QPixmap('kkk.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_texto.setText("Você Digitou: " + conteudo)


aplicacao = QApplication(sys.argv)
app = App()
sys.exit(aplicacao.exec_())