import telepot
import openai
from time import sleep

token_bot = "5613790033:AAHCHQv-xQQXIAsXT6KCdROwWNlP7lWpurc"
openai.api_key = "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"

def transcrever_audio(arquivo_audio):
    with open(arquivo_audio, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type in ["audio", "voice"]:
        bot.sendMessage(chat_id, "*Transcrevendo...*", parse_mode="Markdown")
        bot.download_file(msg[content_type]['file_id'], msg[content_type]['file_id'])
        
        texto = transcrever_audio(msg[content_type]['file_id'])
        bot.sendMessage(chat_id, texto)

bot = telepot.Bot(token_bot)
bot.message_loop(principal)

while 1:
    sleep(5)

