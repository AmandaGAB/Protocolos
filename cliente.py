import socket
from threading import Thread
import threading
from datetime import *


#-------------------------> Servidor aceita conexão? <--------------------------

def aceitarConexao():
    while 1:
        matricula = input('Digite a sua matrícula:')
        clienteSocket.send(str(matricula).encode())
        ok = clienteSocket.recv(1024).decode()
        if ok == 'ok':
            print(clienteSocket.recv(1024).decode()) 
            nomeAluno = input('Digite o seu nome:')
            clienteSocket.send(nomeAluno.encode()) 
            print(clienteSocket.recv(1024).decode())
            recebe = threading.Thread(target = receberResposta, args = ())
            recebe.start()
            envia = threading.Thread(target = enviarPedido, args = ())
            envia.start()
        break


#-------------------------> Recebe resposta do servidor <--------------------------

def receberResposta():
    while True:
        op = clienteSocket.recv(1024).decode()
        if op == '1':
            print(clienteSocket.recv(1024).decode())
        if op == '2':
            print(clienteSocket.recv(1024).decode())
            print(clienteSocket.recv(1024).decode())
            print(clienteSocket.recv(1024).decode())
            print(clienteSocket.recv(1024).decode())

            


#-------------------------> Envia pedidos ao servidor <--------------------------

def enviarPedido():
    a = True 
    while a:
        op = input('Digite 1- tempo ou 2- sair:')
        clienteSocket.send(op.encode())
        if op == '2':
            a = False
        

#-------------------------> Cria socket e inicia thread <--------------------------

clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = input('Digite o nome do host(servidor):') 
# porta = int(input('Digite o número da porta:'))
host = '127.0.0.1'
porta = 8080
clienteSocket.connect((host, porta))
verificar = threading.Thread(target=aceitarConexao).start()

