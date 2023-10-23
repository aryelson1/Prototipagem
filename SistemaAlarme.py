import RPi.GPIO as GPIO
import time
import asyncio
from telegram import Bot

# Configuração do bot
bot_token = '6564692175:AAHXb1-1LLWXtLSw9wrpg52YOpz2neHctWQ'  # Token do Bot
lista_id = ['1622322437','6546123873', '5201121335'] #ID dos usuarios






pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        input_state = GPIO.input(pin)

        if input_state == GPIO.LOW:
            async def enviar_mensagem():
                #Criando o bot
                bot = Bot(token=bot_token)

                #Mensagem
                mensagem = 'ALARME ACIONADO'

                #Envio da mensagem
                for i in lista_id:
                    await bot.send_message(chat_id=i, text=mensagem)

            # Execute a função assíncrona
            loop = asyncio.get_event_loop()
            loop.run_until_complete(enviar_mensagem())
            time.sleep(5)
            
except KeyboardInterrupt:
    GPIO.cleanup()
