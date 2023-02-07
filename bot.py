#########################################################
from config import bot
import config
from time import sleep
import re
import logic
#import control_service.db as db
from telebot import types
from time import sleep
import sqlite3
#from conexion import conn
#########################################################
#if __name__ == '__main__':
#    db.Base.metadata.create_all(db.engine)
#########################################################

# Aquí vendrá la implementación de la lógica del bot
@bot.message_handler(commands=['menu'])
def on_command_menu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('/Si')
    itembtn2 = types.KeyboardButton('/No')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Hola, soy un \U0001F916, ¿cómo estás?, gracias por comunicarse con Control Service Car el Primer\n"
                     "sistema de seguimiento de servicios para su vehículo, ¿Eres un usuario nuevo? Selecciona una opción del menú, Si o No:\n", reply_markup=markup)

@bot.message_handler(commands=['Si'])
def on_command_imc(message):
    response = bot.reply_to(message, "Ingresa tu nombre y tipo de usuario")
    bot.register_next_step_handler(response, proceso_registrar_usuario)

@bot.message_handler(commands=['No'])
def on_command_imc(message):
    response = bot.reply_to(message, "Ingresa el nombre de usuario ya registrado")
    bot.register_next_step_handler(response, proceso_login_usuario)
    
def proceso_registrar_usuario(message):
    try:
        nombre = text(message.text)
        record = bot_data[message.chat.id]
        record.nombre = nombre
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        response = bot.reply_to(message, '¿cual es tu nombre?',
        reply_markup=markup)
        bot.register_next_step_handler(response, process_gender_step)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def proceso_login_usuario(message):
    try:
        usuario = float(message.text)
        record = bot_data[message.chat.id]
        record.usuario = usuario
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Registrar Vehiculos', 'Registrar SOAT, Registrar Repuestos')
        response = bot.reply_to(message, 'hola bievenidoa Control Service Car, estas son las funciones que puedes hacer:',
        reply_markup=markup)
        bot.register_next_step_handler(response, proceso_menu)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")


@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F916, ¿cómo estás?, gracias por comunicarse con Control Service Car el Primer sistema de seguimiento de servicios para su vehículo\n"
        "¿Eres un usuario nuevo? Si o No\n",
        parse_mode="Markdown")
    
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*Aquí podrás registrar Dueños de Empresa, Dueños de Vehículos, Mecánicos, Seguros a los Vehículos, Repuestos y los Servicios realizados por los mecánicos.\n"
        )
    bot.send_message(
        message.chat.id,
        response,
        parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.reply_to(
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste.")
   
#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################