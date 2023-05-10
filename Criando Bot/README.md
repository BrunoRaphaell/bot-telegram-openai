# Como criar bots no telegram

## Conhecendo o `BotFather`

Instale o app em seu smartphone e o execute. A tela inicial será essa:

![](https://i.imgur.com/ouKLtAM.png)

Na barra de pesquisa, digite e pesquise pelo perfil `@BotFather`. Ele é o bot que irá criar o seu bot. É com esse bot que iremos configurar e se nescessário excluir os bots.

Certifique-se que clicou no usuário correto. O perfil do `@BotFather` possui um selo de verificação azul, indicando que é o perfil oficial do bot, conforme imagem abaixo: 

![](https://i.imgur.com/h5fxBEQ.png)

Ao clicar sobre ele você verá uma mensagem com o título "O que esse bot pode fazer por você?" e ao final terá um botão `Iniciar`. Clique nele para iniciar a conversa com o bot.

![](https://i.imgur.com/2hTD3FX.png)

Após clicar em iniciar o `@BotFather` irá enviar uma mensagem de boas vindas e uma lista de comandos que ele entende.

![](https://i.imgur.com/UJpfLlz.png)

A mensagem retornada é:

Eu posso ajudá-lo a criar e gerenciar bots do Telegram. Se você é novo na Bot API, consulte o manual (https://core.telegram.org/bots).

Você pode me controlar enviando estes comandos:

/newbot - criar um novo bot
/mybots - editar seus bots

**Editar Bots**
/setname - alterar o nome de um bot
/setdescription - alterar a descrição do bot
/setabouttext - alterar as informações sobre o bot
/setuserpic - alterar a foto de perfil do bot
/setcommands - alterar a lista de comandos
/deletebot - excluir um bot

**Configurações do Bot**
/token - gerar um token de autorização
/revoke - revogar o token de acesso do bot
/setinline - ativar/desativar o modo inline (https://core.telegram.org/bots/inline)
/setinlinegeo - ativar/desativar solicitações de localização inline (https://core.telegram.org/bots/inline#location-based-results)
/setinlinefeedback - alterar as configurações de feedback inline (https://core.telegram.org/bots/inline#collecting-feedback)
/setjoingroups - permitir que seu bot seja adicionado a grupos?
/setprivacy - ativar/desativar o modo de privacidade (https://core.telegram.org/bots/features#privacy-mode) em grupos

**Aplicativos Web**
/myapps - editar seus aplicativos web (https://core.telegram.org/bots/webapps)
/newapp - criar um novo aplicativo web (https://core.telegram.org/bots/webapps)
/listapps - obter uma lista de seus aplicativos web
/editapp - editar um aplicativo web
/deleteapp - excluir um aplicativo web existente

**Jogos**
/mygames - editar seus jogos (https://core.telegram.org/bots/games)
/newgame - criar um novo jogo (https://core.telegram.org/bots/games)
/listgames - obter uma lista de seus jogos
/editgame - editar um jogo
/deletegame - excluir um jogo existente

## Criando um bot

Para criar um bot, digite o comando `/newbot` e envie. O `@BotFather` irá pedir um nome para o bot. Escolha um nome e envie. Escolhi para o nome do bot `quinta_com_dados` 

Em seguida o `@BotFather` irá pedir um nome de usuário para o bot. Esse nome deve terminar com a palavra `bot` e não pode conter espaços. Escolha um nome e envie. Na imagem eu coloquei `quinta_com_dados_bot`. Mesmo que não seja
obrigatório, uma sugestão para que você sempre se lembre do
nome de usuário do bot é usar o mesmo nome com a terminação
“bot”. Isso apenas servirá para identificá-lo por ocasião
de alteração das configurações.

![](https://i.imgur.com/h6oYe0Z.png)

Ao enviar o nome de usuário do seu bot para o `@BotFather`, você receberá uma mensagem de congratulações juntamente com o token de acesso (token to access) do seu bot. Este token é necessário para programar o bot e informar a conta em que ele deve se conectar ao Telegram. Certifique-se de anotá-lo em um lugar seguro, pois ele permite acesso às configurações, informações e controle do seu bot, além de permitir que você se conecte ao Telegram usando a conta do bot.

Ele também deixa um recado importante "Mantenha seu token seguro e armazene-o com segurança, ele pode ser usado por qualquer pessoa para controlar seu bot."

É esse token que vamos utilizar para programar nosso bot. 

Agora você pode inserir os comandos `/setname`, `/setdescription`, `/setabouttext`, `/setuserpic` e `/setcommands` para configurar o seu bot.


