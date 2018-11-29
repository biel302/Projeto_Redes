from socket import *
from _thread import *
import threading

print_lock = threading.Lock()

def verificarLogin(login, senha, lista):
    if login not in lista:
        return "1"
    else:
        for x in range(0, len(lista)):
            if login == lista[x] and senha == lista[x+1]:
                return "2"
        return "3"

def tokenizar(string):
    lista = []
    palavra = ""
    for x in string:
        if x != ";" :
            palavra += x
        else:
            lista.append(palavra)
            palavra = ""
          
    if palavra != '':
            lista.append(palavra)
    
    return lista

def connection(client):
    arq = open("server.txt", "a")
    arq.close()
    
    arq = open("server.txt", "r")
    lista = arq.readlines()
    lista = tokenizar(lista)
    print(lista)
    arq.close()

    arq = open("server.txt", "a")
    verify = False
    
    while True:
        
        data = client.recv(1024)
        
        while verify == False:
            verification = data.decode()
            verification = tokenizar(verification)
            
            login = verification[0]
            senha = verification[1]
            
            existe = verificarLogin(login, senha, lista)

            if existe == "2":
                msg = "Olá {}!".format(login)
                client.send(msg.encode())
                verify = True
                
            elif existe == "3":
                msg = "Senha errada!"
                client.send(msg.encode())
                
            else:
                msg = "Seja bem vindo ao servidor!"
                arq.write(login + ";" + senha)
                client.send(msg.encode())
                verify = True
            
        print("Mensagem recebida por {}: {}".format(login, data.decode()))
        if not data:
            print('Finalizando Conexão')
            break

        data = data + b' OK'
        client.send(data)
    client.close()
    arq.close()
    

def main():
    
    IPV4 = AF_INET
    TCP = SOCK_STREAM
    
    host = gethostname()
    skt = socket(IPV4, TCP)
    porta = int(input("Qual porta deseja bindar? "))
    skt.bind((host,porta))
    print ('Bind sucess')
    
    skt.listen(3)

    while True:
        conexao, adr = skt.accept()
        
        
        print("Conexão recebida com", str(adr))
        #arquivo = open(str(adr).txt, "wb")

        start_new_thread(connection, tuple([conexao]))
    skt.close

if __name__ == '__main__':
    main()

