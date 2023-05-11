# Criando o bot

Para o desenvolvimento do projeto vamos utilizar o vscode. Caso você ainda não o tenha instalado deixo o artigo: [VisualStudio Code: instalação, teclas de atalho, plugins e integrações](https://www.alura.com.br/artigos/visualstudio-code-instalacao-teclas-de-atalho-plugins-e-integracoes) como conteúdo complementar. 

## Exemplo inicial para as pessoas entenderem como funciona

Antes de tudo vamos criar um ambiente virtual e instalar as bibliotecas necessárias para o projeto. Para isso, execute o seguinte comando no diretório onde estiver o arquivo `requirements.txt`:

```bash
sudo apt install python3-virtualenv
```

```bash
virtualenv <nome_do_ambiente>
source <nome_do_ambiente>/bin/activate
```

```bash
pip install -r requirements.txt
```
Vamos precisar instalar a seguinte biblioteca em nosso Ubuntu:

```bash
sudo apt install ffmpeg
```

O comando "sudo apt-get install ffmpeg" é utilizado para instalar a biblioteca FFmpeg no sistema operacional Ubuntu ou em outros sistemas operacionais baseados em Debian.

A biblioteca FFmpeg é uma coleção de bibliotecas e ferramentas para processar áudio e vídeo. Ela é usada para converter, gravar e transmitir áudio e vídeo em diferentes formatos, além de ser capaz de capturar e transmitir fluxos de áudio e vídeo em tempo real.

**Código inicial:**

```python

import telepot
from time import sleep

token_bot = "5613790033:AAHCHQv-xQQXIAsXT6KCdROwWNlP7lWpurc"

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)    
    mensagem = msg['text']
    
    if mensagem.upper() == 'OI':
        bot.sendMessage(chat_id, 'Olá, tudo bem?')
    else:
        bot.sendMessage(chat_id, 'Não entendi o que você disse')

    
bot = telepot.Bot(token_bot)

bot.message_loop(principal)

while 1:
    sleep(5)
```

[Documentação telepot](https://telepot.readthedocs.io/en/latest/)

Os campos `content_type` , `chat_type` e `chat_id` são retornos do método glance da classe Telepot, que extrai as informações sobre a mensagem recebida.

`content_type` define o tipo de conteúdo da mensagem, que pode ser:

- Mensagens de texto: text (texto)
- Mensagens de áudio: audio (áudio)
- Documentos: document (documento)
- Jogos: game (jogo)
- Fotografias: photo (fotografia)
- Adesivos: sticker (adesivo)
- Vídeos: video (vídeo)
- Mensagens de voz: voice (voz)
- Notas de vídeo: video_note (nota de vídeo)
- Contatos: contact (contato)
- Localizações: location (localização)
- Locais: venue (local)
- Novos membros de chat: new_chat_member (novo membro de chat)
- Membros que deixaram o chat: left_chat_member (membro que deixou o chat)
- Novos títulos de chat: new_chat_title (novo título de chat)
- Novas fotos de chat: new_chat_photo (nova foto de chat)
- Exclusão de foto de chat: delete_chat_photo (exclusão de foto de chat)
- Criação de grupo de chat: group_chat_created
- Criação de supergrupo de chat: supergroup_chat_created
- Criação de canal de chat: channel_chat_created
- Migração para outra chat_id: migrate_to_chat_id
- Migração a partir de outra chat_id: migrate_from_chat_id
- Mensagem fixada: pinned_message (mensagem fixada)
- Novos membros de chat: new_chat_members (novos membros de chat)
- Faturas: invoice (fatura)
- Pagamento com sucesso: successful_payment (pagamento com sucesso)


Na variável `chat_id`, é armazenada a identificação exclusiva do chat, seja ele uma conversa direta com um usuário ou um grupo em que o bot esteja inserido. Ao responder, é fundamental utilizar essa identificação para garantir que a mensagem seja enviada para o destinatário correto, seja ele um usuário ou um grupo.

Para que a mensagem seja enviada para o usuário ou grupo correto, o método `sendMessage` requer que o `chat_id` seja especificado. Além disso, é necessário informar o texto da mensagem que se deseja enviar.

Após finalizar a nossa função principal, precisamos criar um objeto chamado "bot" utilizando a seguinte linha de código: `bot = telepot.Bot('TOKEN_DE_ACESSO')`

Para que essa linha funcione corretamente, é importante que você tenha criado o seu próprio bot no Telegram e tenha gerado um token de acesso para ele, conforme explicado anteriormente.

Para que o objeto "bot" envie as mensagens para a função principal e elas possam ser tratadas, utilizamos a seguinte linha de código: `bot.message_loop(principal)`. Com isso, criamos um laço (loop) onde cada mensagem recebida deverá ser processada pela função principal.

Apesar de já termos finalizado a codificação, nosso programa ainda não possui o comportamento desejado. Quando executado, ele simplesmente terminaria depois da última linha.

Para garantir que o bot permaneça em funcionamento, receba as mensagens e as processe quando necessário, é necessário criar um loop infinito que permita que o programa fique sempre em execução.

Para isso, podemos utilizar as seguintes linhas de código:

```
while True:
    sleep(5)  # Espera por 5 segundos antes de processar as próximas instruções
```

Dessa forma, o bot continuará em execução indefinidamente, aguardando novas mensagens para serem tratadas. A instrução time.`sleep(5)` faz com que o programa espere 5 segundos antes de processar as próximas instruções, evitando que o bot consuma muitos recursos do sistema.
 
[Link para converter unix para timestamp](https://www.epochconverter.com/)

## Criando bot para transcrever áudio


Vamos utilizar a API da OpenAI para transcrever áudios enviados ao nosso bot. Para isso, acesse a [página da API](https://platform.openai.com/docs/api-reference). Se você ainda não fez o login, é necessário fazê-lo antes para ter acesso ao conteúdo.

Primeiro passo é fazer a instalação da biblioteca do openAI

```bash
pip install openai
```

Como referência para a criação de um modelo capaz de transcrever áudio vamos usar as refrências abaixo:

- [Criar transcrição](https://beta.openai.com/examples/default-example-1)
- [Aprenda como transformar áudio em texto](https://platform.openai.com/docs/guides/speech-to-text)

Nesse segundo link você vai encontrar todas os idiomas que o modelo é capaz de transcrever.

O modelo que vamos utilizar é o [Whisper](https://openai.com/research/whisper) que é capaz de trasncrever e traduzir áudios. Para trasncrição vamos utilizar o exemplo que a documentação fornece:

```python
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
audio_file= open("/path/to/file/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
```

*Obs: O modelo suporta os seguintes formatos de áudio `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav` e `webm`.*

*Obs: Conforme aviso acima, certifique-se que você está utilizando a versão 0.27.0 da biblioteca do openAI. Para isso, execute o comando abaixo:*

```bash
pip freeze | grep openai
```

Caso não esteja atualize com o seguinte comando: 

```bash
pip install --upgrade openai
```

Pronto! Alinhada as expectativas vamos para o código.