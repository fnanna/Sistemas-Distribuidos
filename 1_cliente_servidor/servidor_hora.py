import socket
from datetime import datetime
import threading

HOST = "127.0.0.1"
PORT = 8000

def atende_cliente(conn,addr):
    with conn:
        print(f"Conectado por {addr}")
        dado = conn.recv(1024)
        hora = datetime.now().strftime('%H:%M:%S')
        conn.sendall(hora.encode('utf-8')) #envia como bytes


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: #with para nao precisar de servidor.close()
    servidor.bind((HOST,PORT))
    servidor.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    while True:
        conn, addr = servidor.accept()
        t = threading.Thread(target=atende_cliente, args=(conn, addr), daemon=True)
        t.start()
        