import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = []
lock = threading.Lock() #usa em todos os lugares que altera clientes[] para tratar concorrencia

def broadcast(mensagem, remetente):
    with lock:
        destinatarios = list(clientes) #copia lista
    for c in destinatarios:
        if c != remetente: #envia a mensagem para todos, menos o remetente
            c.sendall(mensagem)

def conecta_cliente(conn,addr):
    print(f"{addr} conectou")
    try:   
        while True:
            dado = conn.recv(1024)
            if not dado: # cliente desconectou
                break
            broadcast(dado, conn)
    except ConnectionResetError: #conexao cai
        pass
    finally:
        with lock:
            if conn in clientes:
                clientes.remove(conn)
        print(f"{addr} desconectou")
        conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST,PORT))
    servidor.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()
        with lock: 
            clientes.append(conn)

        t = threading.Thread(target=conecta_cliente, args=(conn, addr), daemon=True)
        t.start()
        