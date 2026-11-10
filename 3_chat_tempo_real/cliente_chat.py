import socket
import threading

HOST = "127.0.0.1"  
PORT = 8000  

def receber(socket):
    while True:
        try:
            dado = socket.recv(1024)
        except OSError:
            break  # socket fechado pela thread 
        
        if not dado:
            break
        print(dado.decode('utf-8'))

def enviar(socket):
    while True:
        texto = input()
        if not texto:
            continue
        socket.sendall(texto.encode('utf-8'))

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    #adiciona um apelido ao entrar  no chat:
    apelido = ""
    while not apelido:
        apelido = input("Escolha seu apelido: ").strip()
        if not apelido:
            print("O apelido não pode ser vazio.")
    cliente.sendall(apelido.encode("utf-8"))

    print("Conectado. Digite sua mensagem: ")
    #thread que fica recebendo as mensagens:
    t = threading.Thread(target=receber, args=(cliente,), daemon=True)
    t.start()
    
    #envia as mensagens (rodando na thread principal):
    try:
        enviar(cliente)
    except (KeyboardInterrupt, EOFError): # crl c para encerrar
        pass
    except OSError: # servidor encerra
        print("Erro ao enviar: conexão perdida.")
    finally:
        cliente.close()
        print("Desconectado.")

if __name__ == "__main__":
    main()