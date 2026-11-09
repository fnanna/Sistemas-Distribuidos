import rpyc

conn = rpyc.connect('localhost', 18861)
hora = conn.root.get_hora()
print(f'Hora: {hora}')
conn.close()