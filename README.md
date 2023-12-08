# pytbot
Uma simples biblioteca que utiliza da api do telegram para facilitar o desenvolvimento de bots.

## Como instalar
```
git clone https://github.com/nexzydev/pytbot
cd pytbot
```

## Como usar
* Iniciando
  - Codigo exemplo está no arquivo pytbot.py
  - Primeiro, importe a classe Bot: ```from src.init import Bot```
  - Após isso, inicie o bot assim: ```bot = Bot("SEU_TOKEN_AQUI")```
  - > Agora leia a documentação da classe Bot.
* Documentação
  - Você pode ver diretamente [aqui](https://github.com/nexzydev/pytbot/blob/main/src/init.py) ou pode continuar lendo isso.
  - Funções
    - ```send_text(chat_id="ID_DO_CHAT", text="Hello world", parsemode="Markdown")``` -> Envia uma mensagem
    - ```command(command_name="/exemplo")``` -> Verifica se um comando foi enviado, se foi enviado retorna uma lista contendo chat_id, command, message_id
   
# Creditos
Created by nexzy
