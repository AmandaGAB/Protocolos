import socket
from threading import Thread
import threading
from datetime import *


#-------------------------> Tratamento de pedidos <--------------------------

def controleResposta(conexaoAluno, endereco):
    while True:
        try:
            op = conexaoAluno.recv(1024).decode()
            if op == '1':
                conexaoAluno.send('1'.encode())
                conexaoAluno.send(str(datetime.now()).encode())
            elif op == '2':
                conexaoAluno.send('2'.encode())
                conexaoAluno.send('Você está deixando a sala!.'.encode())
                time = datetime.now()
                conexaoAluno.sendall(str(nomesAlunos[conexaoAluno]).encode()+' saiu da sala em '.encode()+str(time).encode())
                sair(conexaoAluno,endereco, time)
                
        except:
            conexao.close()


#-------------------------> Remover uma conexão <--------------------------------    

def sair(conexao, endereco, time):
    nome = nomesAlunos[conexao]
    print(f'O aluno: {nome} - {endereco} saiu da sala em {time} ')
    conexoes.remove(conexao)
    

    
#-------------------------> Retorna matrícula <----------------------------------
   
def existe(matricula):
    matriculas = open("matriculas.txt", 'r')
    ler = matriculas.read().splitlines()
    for i in range(len(ler)):
        if ler[i] == matricula:
            return ler[i]

#-------------------------> Verifica matríula existente <-----------------

def verifica():
    matricula = conexao.recv(1024).decode()
    if existe(matricula) == matricula:
        conexao.send(('ok'.encode()))
        conexao.send('Matrícula existente!'.encode())
        nomeAluno = conexao.recv(1024).decode() 
        nomesAlunos[conexao] = nomeAluno 
        conexao.send('Você entrou na sala'.encode())
        print('Conexão estabelecida com:', nomeAluno)
        threading.Thread(target=controleResposta, args=(conexao, endereco)).start()
    else:
        print('Informações incorretas')
        conexao.close()
    
#-----------------------------> Realizar comunicação <------------------------------------------

# host = socket.gethostbyname(socket.gethostname())
host = '127.0.0.1'
porta = int(input('Digite o número da porta:'))
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServidor.bind((host, porta))
socketServidor.listen(20)
conexoes = []
nomesAlunos = {}
print(f'Porta: {porta}------Host:{host}')
while True:
    conexao, endereco = socketServidor.accept()
    print("Conexão recebida:" ,endereco[1] )
    conexoes.append(conexao)
    verificar = threading.Thread(target=verifica).start()
        

