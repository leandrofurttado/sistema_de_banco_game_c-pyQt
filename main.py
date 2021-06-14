from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from login_design import *
from design_banco import *
from design_transferencia import *
import sys
import json
from time import sleep


class Aplicacao1(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.janela2 = Janela2()
        self.buttonLogin.clicked.connect(self.checagem)
        self.buttonRegister.clicked.connect(self.registrar)

    def registrar(self):
        with open('clientes.json', 'r') as ArquivoClientes:
            dadosclientes = json.load(ArquivoClientes)
            ArquivoClientes.close()

        with open('clientes.json', 'w') as ArquivoClientes:
            dadosclientes[f'{self.inputNomeBancario.text()}'] = [int(self.inputContaBanco.text()), 0]
            json.dump(dadosclientes, ArquivoClientes)
            self.label_Error.setText(F'VOCÊ REGISTROU!({self.inputNomeBancario.text()}:{self.inputContaBanco.text()})')

    def checagem(self):
        with open('clientes.json', 'r') as ArquivoClientes:
            self.listaRegistrados = json.load(ArquivoClientes)
            if self.inputNomeBancario.text() in self.listaRegistrados.keys()\
                    and int(self.inputContaBanco.text()) == self.listaRegistrados[f'{self.inputNomeBancario.text()}'][0]:
                with open('save.txt', 'w') as save_login:
                    save_login.write(f'{self.inputNomeBancario.text()}\n{self.inputContaBanco.text()}')
                self.label_Error.setText('LOGADO!')
                sleep(0.5)
                self.janela2.show()
                self.hide()

            else:
                self.label_Error.setText('ESSA CONTA NÃO EXISTE!')


class Janela3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela3()
        self.ui.setupUi(self)
        self.ui.button_Transferencia.clicked.connect(self.Transferir)

    def Transferir(self):
        with open('clientes.json', 'r') as ArqSaldo:
            dict_cliente = json.load(ArqSaldo)
                #########ACIMA É OS DADOS DA CONTA LOGADA
        with open('save.txt', 'r') as ArqSave:
            lista_login = ArqSave.readlines()
            usuario_atual = lista_login[0].replace('\n', '')
            saldo_cliente = dict_cliente[f'{usuario_atual}'][1]
            try:
                if dict_cliente[f'{self.ui.inputNomeTrans.text()}'][0] == int(self.ui.inputContaTrans.text()):
                    with open('clientes.json', 'w') as ArqSaldo:
                        if dict_cliente[f'{usuario_atual}'][1] < int(self.ui.inputQuantiaTrans.text()):
                            self.ui.label_ErrorTrans.setStyleSheet('color: red')
                            self.ui.label_ErrorTrans.setText(f'Você não possui R${self.ui.inputQuantiaTrans.text()}'
                                                             f' para transferir!')
                            json.dump(dict_cliente, ArqSaldo)
                        else:
                            saldo_destinatario = dict_cliente[f'{self.ui.inputNomeTrans.text()}'][1]
                            saldo_destinatario = saldo_destinatario + int(self.ui.inputQuantiaTrans.text())
                            dict_cliente[f'{self.ui.inputNomeTrans.text()}'][1] = saldo_destinatario
                            dict_cliente[f'{usuario_atual}'][1] -= int(self.ui.inputQuantiaTrans.text())
                            json.dump(dict_cliente, ArqSaldo)
                            self.ui.label_ErrorTrans.setStyleSheet('color: green')
                            self.ui.label_ErrorTrans.setText('Você transferiu com sucesso!')
                else:
                    self.ui.label_ErrorTrans.setStyleSheet('color: red')
                    self.ui.label_ErrorTrans.setText('NOME correto! Porém CONTA não identificada.')
            except Exception as error:
                self.ui.label_ErrorTrans.setStyleSheet('color: red')
                self.ui.label_ErrorTrans.setText('ERRO! NOME E CONTA PROVAVELMENTE NÃO EXISTE!')


class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Janela2()
        self.ui.setupUi(self)
        self.janela3 = Janela3()
        self.ui.button_FazerDeposito.clicked.connect(self.depositar)
        self.ui.buttonSacar.clicked.connect(self.sacar)
        self.ui.button_verSaldo.clicked.connect(self.verSaldo)
        self.ui.buttonTransferencia.clicked.connect(self.transferirDinheiro)


    def transferirDinheiro(self):
        self.janela3.show()


    def verSaldo(self):
        with open('clientes.json', 'r') as ArqSaldo:
            dict_cliente = json.load(ArqSaldo)
            with open('save.txt', 'r') as ArqSave:
                usuario_senha = ArqSave.readlines()
                usuario_atual = usuario_senha[0].replace('\n', '')
                saldo_cliente = dict_cliente[f'{usuario_atual}'][1]
                self.ui.label_Saldo.setText(f'R${str(saldo_cliente)}')

    def depositar(self):
        with open('clientes.json', 'r') as ArqSaldo:
            dict_cliente = json.load(ArqSaldo)
            with open('save.txt', 'r') as ArqSave:
                lista_login = ArqSave.readlines()
                usuario_atual = lista_login[0].replace('\n', '')
                saldo_cliente = dict_cliente[f'{usuario_atual}'][1]

                #ABRIU TODOS OS ARQUIVOS E PEGOU O SALDO DO DICIONARIO DO CLIENTE.
                #AGORA VAMOS FAZER A VERDADEIRA FUNÇÃO DE DEPOSITO.
                saldo_cliente += int(self.ui.inputValor.text())
                self.ui.label_Saldo.setText(f'R${str(saldo_cliente)}')
                self.ui.label_DeErro.setStyleSheet("color: rgb(89, 255, 0); font: 18pt \"Verdana\";")
                self.ui.label_DeErro.setText(f'Você depositou R${self.ui.inputValor.text()}!')
                ArqSaldo.close()
                ArqSave.close()

        #AGORA TEMOS QUE SALVAR O ACRÉSCIMO NA CONTA:
        with open('clientes.json', 'w') as ArqSaldo:
            with open('save.txt', 'r') as ArqSave:
                lista_login = ArqSave.readlines()
                usuario_atual = lista_login[0].replace('\n', '')
                dict_cliente[f'{usuario_atual}'][1] = saldo_cliente
                json.dump(dict_cliente, ArqSaldo)


    def sacar(self):
        with open('clientes.json', 'r') as ArqSaldo:
            dict_cliente = json.load(ArqSaldo)
            with open('save.txt', 'r') as ArqSave:
                lista_login = ArqSave.readlines()
                usuario_atual = lista_login[0].replace('\n', '')
                saldo_cliente = dict_cliente[f'{usuario_atual}'][1]
                if saldo_cliente < int(self.ui.inputValor.text()):
                    sleep(1)
                    self.ui.label_DeErro.setStyleSheet("color: red; font: 18pt \"Verdana\";")
                    self.ui.label_DeErro.setText('Você não tem esse valor!')
                else:
                    sleep(1)
                    saldo_cliente -= int(self.ui.inputValor.text())
                    self.ui.label_Saldo.setText(f'R${str(saldo_cliente)}')
                    self.ui.label_DeErro.setStyleSheet("color: rgb(89, 255, 0); font: 18pt \"Verdana\";")
                    self.ui.label_DeErro.setText(f'Você sacou R${self.ui.inputValor.text()}!')

        with open('clientes.json', 'w') as ArqSaldo:
            with open('save.txt', 'r') as ArqSave:
                lista_login = ArqSave.readlines()
                usuario_atual = lista_login[0].replace('\n', '')
                dict_cliente[f'{usuario_atual}'][1] = saldo_cliente
                json.dump(dict_cliente, ArqSaldo)




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Aplicacao1()
    app.show()
    qt.exec_()
