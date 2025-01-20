# WebSockets & [Socket.IO](https://socket.io/get-started/chat)

[project](/basic-applications/socketio)
[fastapi & socket.io](https://github.com/pyropy/fastapi-socketio)

`WebSocket` é um protocolo de comunicação bidirecional, em tempo real baseado em `TCP`
projetado para permitir uma comunicação entre client e servidor. Ele é ideal para cenários onde é necessário manter uma conexão aberta para troca contínua de dados, reduzindo a latência e o overhead
causados por múltiplas requisições `HTTP`.

> Vantagens:

- Comunicação em tempo real.

- Elimina a necessidade de repetidos `handshakes HTTP`.

- Requer menos largura de banda em relação a tecnologias como [`Long Polling`](https://dev.to/brinobruno/.real-time-web-communication-longshort-polling-websockets-and-sse-explained-nextjs-code-1l43).

- Compatível com a maioria dos navegadores e linguagens back-end.

> Desvantagens: 

- Implementação mais complexa em relação ao `REST HTTP`.

- Escalar `WebSockets` pode ser desafiador em ambientes distribuídos.

- Cada conexão consome recursos do servidor, limitando o número máximo de conexões simultâneas.


> Boas Práticas ao Impmlementar `WebSockets`:

- Monitorar conexões ativas e implementar reconexões automáticas em caso de falha.

- Use `WSS` (WebSocket Secure) para criptografar a comunicação.

- Valide os dados recebidos para evitar ataques de injeção de código.

- Use ferramentas para gerenciar mensagens entre servidor e cliente.

- Implemente limitação de recursos.

