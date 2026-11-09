import socket
from datetime import datetime
import threading

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: #with para nao precisar de servidor.close()
    servidor.bind((HOST,PORT))
    servidor.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    while True:
        conn, addr = servidor.accept()
        with conn:
                print(f"Conectado por {addr}")
                dado = conn.recv(1024).decode('utf-8')
                texto = dado[::-1]
                conn.sendall(texto.encode('utf-8'))
        