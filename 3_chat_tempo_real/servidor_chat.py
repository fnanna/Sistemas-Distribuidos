import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = []

def broadcast(mensagem, remetente):
    for c in clientes:
        if c != remetente: #envia a mensagem para todos, menos o remetente
            c.sendall(mensagem)

def conecta_cliente(conn,addr):
    print(f"{addr} conectou")
    try:
        while True:
            dado = conn.recv(1024)
            if not dado: # cliente desconectou
                clientes.remove(conn)
                break
            
            texto = dado.decode('utf-8')
            broadcast(texto.encode("utf-8"), conn)
    except ConnectionResetError: #conexao cai
        clientes.remove(conn)
        pass
    finally:
        print(f"{addr} desconectou")
        conn.close()


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST,PORT))
servidor.listen()
print(f"Servidor escutando em {HOST}:{PORT}")
while True:
    conn, addr = servidor.accept()
    clientes.append(conn)
    t = threading.Thread(target=conecta_cliente, args=(conn, addr), daemon=True)
    t.start()
servidor.close()
        