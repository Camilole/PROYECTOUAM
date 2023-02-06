#########################################################
import telebot
import logging
from decouple import config

#########################################################

#Bot version
VERSION= 0.1

#TOKEN desde archivo de configuración

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

#########################################################

# Se crea el objeto bot utilizando el Token

bot = telebot.TeleBot(TELEGRAM_TOKEN)

#Determina el nivel de los mensajes que se van a mostrar
telebot.logger.setLevel(logging.INFO)

#########################################################
