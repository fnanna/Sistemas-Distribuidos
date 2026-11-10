# Parte II: Cliente/Servidor com RPyC

Implementação em Python do mesmo serviço de horário da Parte I, usando chamada de procedimento remoto (RPC) com a biblioteca RPyC.

## Como funciona

O servidor expõe o método `exposed_get_hora`, que retorna o horário atual. O cliente se conecta, chama `get_hora()` como se fosse uma função local, imprime o resultado e encerra. O método é executado no servidor, e o cliente recebe só o retorno.

## Como executar

Requer a biblioteca RPyC: `pip install rpyc`.

1. Em um terminal, inicie o servidor:
   ```
   python servidor_rpyc.py
   ```
2. Em outro terminal, execute o cliente:
   ```
   python cliente_rpyc.py
   ```

## Resultado

O cliente imprime o horário no formato `HH:MM:SS` e encerra. O servidor continua em execução.

## Comparação com a Parte I

Anteriormente, foi necessário implementar manualmente `socket`, `bind`, `listen`, `accept`, as threads, o protocolo de mensagens e a conversão entre texto e bytes. Com o RPyC, o `ThreadedServer` cuida da conexão e do multithread, e a serialização é automática. 