import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: #with para nao precisar de servidor.close()
    servidor.bind((HOST,PORT))
    servidor.listen()
    while True:
        conn, addr = servidor.accept()
        with conn:
            print(f"Conectado por {addr}")
            dado = conn.recv(1024)
            hora = datetime.now().strftime('%H:%M:%S')
            conn.sendall(hora.encode('utf-8')) #envia como bytes