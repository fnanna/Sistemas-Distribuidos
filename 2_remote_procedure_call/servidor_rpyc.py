import rpyc
from datetime import datetime
from rpyc.utils.server import ThreadedServer

class HoraService(rpyc.Service):
    def exposed_get_hora(self):
        return datetime.now().strftime('%H:%M:%S')

if __name__ == '__main__':
    servidor = ThreadedServer(HoraService, port=18861) # "encapsula" da criacao do socket ate o sendall() 
    print("Servidor RPyC escutando na porta 18861")
    servidor.start()