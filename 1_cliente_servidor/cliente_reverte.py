import socket

HOST = "127.0.0.1"  
PORT = 8000  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    cliente.sendall(b"Ola, Mundo Distribuido")
    dado = cliente.recv(1024)
    print(dado.decode('utf-8')) 

