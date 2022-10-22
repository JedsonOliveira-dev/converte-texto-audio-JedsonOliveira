from gtts import gTTS
import os

texto = 'Seja bem vindo ao top10 DEV! Não esqueça de se inscrever no canal e ativar o sininho.'

tts = gTTS(texto, lang='pt-br')

tts.save('voz.mp3')
os.system('voz.mp3')
