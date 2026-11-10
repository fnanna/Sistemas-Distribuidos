import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = {}
lock = threading.Lock() #usa em todos os lugares que altera clientes[] para tratar concorrencia

def broadcast(mensagem, remetente):
    with lock:
        destinatarios = list(clientes.keys()) #copia lista

    for c in destinatarios:
        if c is remetente:
            continue
        c.sendall(mensagem.encode("utf-8"))
    

def conecta_cliente(conn,addr):
    apelido = conn.recv(1024).decode("utf-8").strip()
    with lock: 
        clientes[conn]=apelido

    print(f"{addr} conectou ({apelido})")
    broadcast(f"{apelido} entrou no chat", None)

    try:   
        while True: #recebe as mensagens e envia por broadcast
            dado = conn.recv(1024)
            if not dado: # cliente desconectou
                break
            texto = dado.decode("utf-8")
            broadcast(f"{apelido}: {texto}", conn)

    except ConnectionResetError: #conexao cai
        pass
    finally:
        with lock:
            clientes.pop(conn, None)
        print(f"{addr} desconectou")
        conn.close()
        broadcast(f"{apelido} saiu do chat", None)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST,PORT))
    servidor.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()

        t = threading.Thread(target=conecta_cliente, args=(conn, addr), daemon=True)
        t.start()
        