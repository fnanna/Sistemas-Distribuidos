# Parte I: Cliente/Servidor com Sockets

Implementação em Python (TCP, módulo `socket`) de dois serviços.

## 1. Servidor de horário (multithread)

O cliente envia um pedido, o servidor responde com o horário atual e o cliente encerra. O servidor cria uma thread para cada cliente, então atende vários ao mesmo tempo.

- `servidor_hora.py`
- `cliente_hora.py`

## 2. Servidor que reverte strings

O cliente envia `Olá, Mundo Distribuído` e o servidor devolve o texto invertido.

- `servidor_reverse.py`
- `cliente_reverse.py`

## Como executar

Os dois servidores usam a porta 8000, então deve ser rodado **um de cada vez**.

1. Em um terminal, inicie o servidor:
   ```
   servidor_hora.py
   ```
2. Em outro terminal, execute o cliente:
   ```
   cliente_hora.py
   ```

Para o servidor de strings, troque pelos arquivos `servidor_reverse.py` e `cliente_reverse.py`.

## Resultado

- Horário: o cliente imprime a hora no formato `HH:MM:SS`.
- Reverse: o cliente imprime `odíubirtsiD odnuM ,álO`.
