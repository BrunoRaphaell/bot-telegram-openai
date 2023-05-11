Por [Millena Gená Pereira](https://cursos.alura.com.br/user/millenagena):

Retirado do curso [Aprofundando no Airflow: Executores Local e Celery](https://cursos.alura.com.br/course/aprofundando-airflow-executor-kubernetes/task/120943)

## O que é o WSL?

WSL é uma sigla para *Windows Subsystem for Linux* que em português significa Subsistema Windows para Linux. Esse recurso permite instalar e executar uma distribuição Linux diretamente no Windows.

O terminal do WSL pode ser utilizado para executar aplicativos e ferramentas via comandos Linux. Além disso, ele nos permite executar aplicativos do Linux juntamente com os aplicativos da área de trabalho e da loja do Windows e também acessar os arquivos Windows dentro do Linux.

## Pré-requisitos

Para executar os comandos a seguir, você deve estar executando o Windows 10 versão 2004 e superiores ou o Windows 11.

## Instalando o Windows Terminal

O terminal do Windows é um aplicativo que permite utilizar diferentes shells de linha de comando, como o Prompt de Comando, PowerShell e o WSL. Esse terminal nos permite abrir diferentes abas com cada um desses shells e personalizá-los.

Pode ser que você já tenha ele instalado, mas caso não tenha, é importante realizar a instalação pois vamos utilizá-lo no decorrer do curso para abrirmos nosso terminal do WSL. Para instalá-lo é simples, na barra de pesquisa do Windows pesquise por "Microsoft Store":


![Alt text: Captura de tela da barra de pesquisa do Windows com o texto "Microsoft Store" digitado. Acima da barra de pesquisa aparece a opção correspondente ao texto pesquisado, também chamada de "Microsoft Store". Esse aplicativo está destacado por um retângulo vermelho.](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img1.png)

Ao abrir a loja de aplicativos da Microsoft, na barra de pesquisa, pesquise por "Windows Terminal" e selecione a opção "Windows Terminal":


![Alt text: Captura da tela inicial do aplicativo Microsoft Store. Na parte superior central desse app existe uma barra de pesquisa com o texto "Windows Terminal" digitado. Abaixo dessa barra de pesquisa são apresentadas 3 opções correspondentes a pesquisa, a segunda opção está destacada por uma seta vermelha.](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img2.png)

Feito isso, você pode selecionar e instalar essa ferramenta. Uma vez que sua instalação for finalizada, para abrir esse terminal, você pode pesquisar por "Terminal" na barra de pesquisa do Windows:



![Alt text: Captura de tela da barra de pesquisa do Windows com o texto "Terminal" digitado. Acima da barra de pesquisa aparece a opção correspondente ao texto pesquisado, também chamada de "Terminal". Esse aplicativo está destacado por um retângulo vermelho.](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img3.png)


## Instalando o WSL 2

Para começar a instalação do WSL 2 você pode abrir o terminal do Windows que baixamos anteriormente:


![Alt text: Captura de tela da barra de pesquisa do Windows com o texto "Terminal" digitado. Acima da barra de pesquisa aparece a opção correspondente ao texto pesquisado, também chamada de "Terminal". Esse aplicativo está destacado por um retângulo vermelho.](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img3.png)

Feito isso, ele já vai abrir uma aba inicial nesse terminal com o Windows Powershell:


![Alt text: Captura de tela do terminal do Windows Powershell](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img4.png)

Caso por padrão o seu terminal não abra do Powershell, você pode clicar na setinha apontada para baixo, na barra superior do terminal, e selecionar o Powershell:


![Alt text: Captura de tela do terminal do Windows Powershell. Na barra superior do terminal há uma seta para baixo destacada por um retângulo vermelho. Abaixo dessa seta, existem algumas opções e a primeira delas "Windows Powershell" está destacada por um retângulo vermelho.](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img5.png)

Em seguida, podemos executar o comando:

```
wsl --list --online
``` 

Esse comando vai listar algumas versões do Ubuntu disponíveis para instalarmos.


![Alt text: Captura de tela do terminal do Windows Powershell em que o comando "wsl –list –online" foi executado. Como resultado, foram disponibilizados diversos nomes de diferentes distribuições e versões Linux.](https://i.imgur.com/tUDCbsH.png)

Nós vamos instalar a distribuição "Ubuntu-20.04", para isso podemos executar o comando:

```
wsl --install -d Ubuntu-22.04
```

Depois disso, vamos aguardar até que a instalação seja finalizada. Pode ser necessário pressionar a tecla "Enter" em alguns momentos para prosseguir com a instalação. E após a execução desse comando, caso apareça a mensagem "As alterações só terão efeito depois que o sistema for reiniciado." é importante que você reinicie sua máquina para prosseguir.

Caso essa mensagem não apareça, deve ser aberto um segundo terminal semelhante ao da imagem abaixo:


![Alt text: Captura de tela do terminal nomeado como "Ubuntu 20.04 on Windows". Na última linha de texto do terminal, consta "Enter new UNIX username" que em português significa "Entre com seu novo nome de usuário UNIX".](https://caelum-online-public.s3.amazonaws.com/2463-aprofundando-apache-airflow/aula-1/Aula1-img7.png)

Nesse momento, você vai informar o nome de usuário que deseja utilizar no Linux e também sua senha.

E, pronto! Agora temos o WSL funcionando :)

Podemos fechar os terminais abertos e abrir novamente o terminal do Windows. Uma vez nesse terminal, podemos clicar na seta localizada na barra superior e selecionar o "Ubuntu-20.04" para abrirmos o terminal do nosso Linux:


![Alt text: Captura de tela do terminal do Windows Powershell. Na barra superior do terminal há uma seta para baixo destacada por um retângulo vermelho. Abaixo dessa seta, existem algumas opções e a quinta delas "Ubuntu-20.04" está destacada por um retângulo vermelho.](https://i.imgur.com/RvSjprS.png)


Caso queira conhecer mais sobre o WSL, acesse a documentação:

* [Perguntas frequentes sobre o Subsistema Windows para Linux](https://learn.microsoft.com/pt-br/windows/wsl/faq)
