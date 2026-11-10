import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST,PORT))
servidor.listen()
print(f"Servidor escutando em {HOST}:{PORT}")
while True:
    conn, addr = servidor.accept()
    with conn:
            dado = conn.recv(1024)
            texto = dado.decode('utf-8')
            conn.sendall(texto.encode('utf-8'))
servidor.close()
        