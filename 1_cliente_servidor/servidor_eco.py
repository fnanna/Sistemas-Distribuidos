import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: #with para nao precisar de servidor.close()
    servidor.bind((HOST,PORT))
    servidor.listen()
    conn, addr = servidor.accept()
    
    with conn:
        print(f"Conectado por {addr}")
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        conn.sendall(data)