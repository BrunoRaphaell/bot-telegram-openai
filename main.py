import telepot
import openai
import ffmpeg
import os
from time import sleep

# Configuração do OpenAI
openai.api_key = os.environ.get('API_KEY_OPENAI')

# Configuração do bot do Telegram
token = os.environ.get('TOKEN_BOT')
bot = telepot.Bot(token)

# Transcrever áudio usando o OpenAI
def transcrever_audio(arquivo_audio):
    with open(arquivo_audio, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']

# Converter áudio para mp3
def converter_to_mp3(audio_file):
    output_file = audio_file.split(".")[0] + ".mp3"

    stream = ffmpeg.input(audio_file)
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(stream, quiet=True)

# Função principal
def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    formatos_suportados = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']
    if content_type in ["audio", "voice"]:
        bot.sendMessage(chat_id, "*Transcrevendo...*", parse_mode="Markdown")
        
        formato = msg[content_type]['mime_type'].split('/')[1]
        nome_arquivo = msg[content_type]['file_id']+f".{formato}"

        bot.download_file(msg[content_type]['file_id'], nome_arquivo)
        
        if formato not in formatos_suportados:
            converter_to_mp3(nome_arquivo)
            os.remove(nome_arquivo)
            
            texto = transcrever_audio(msg[content_type]['file_id']+".mp3")
            bot.sendMessage(chat_id, texto)
            os.remove(msg[content_type]['file_id']+".mp3")
        else:
            texto = transcrever_audio(msg[content_type]['file_id']+f".{formato}")
            bot.sendMessage(chat_id, texto)
            os.remove(nome_arquivo)
        
# Inicia o bot
bot = telepot.Bot(token)
bot.message_loop(principal)

# Mantém o bot rodando
while 1:
    sleep(5)

