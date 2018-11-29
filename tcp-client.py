from socket import *

def main():
    host = gethostname()
    IPV4 = AF_INET
    TCP = SOCK_STREAM

    skt = socket(IPV4, TCP)
    verificacao = False
    porta = int(input("Insira a porta de destino: "))
    skt.connect((host,porta))
    
    
    while verificacao == False:
        login = input("Digite seu login: ")

        senha = input("Digite sua senha: ")

        usuario = login + ";" + senha
        usuario = usuario.encode()
        
        skt.send(usuario)
        msg = skt.recv(1024)
        msg = msg.decode()
        print(msg)
        if str(msg) != "Senha errada!":
            verificacao = True
    print('Connected')

    while True:
        msg = input("O que deseja fazer? \n 1- ")
        msg = input("O que deseja enviar? ")
        msg = msg.encode('latin-1')

        skt.send(msg)

        data = skt.recv(1024)

        print('Recebido do servidor: ',str(data.decode('latin-1')))

        resposta = input('\nDeseja continuar?(Y/n): ')
        if resposta == 'Y': continue
        else: break

    skt.close()

if __name__ == '__main__': 
    main()

    
