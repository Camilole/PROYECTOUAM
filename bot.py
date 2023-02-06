#######################################################################

from config import bot
import config
from time import sleep
import re
import logic.logic as logic
from telebot import types


#######################################################################
# Commando start 

@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_welcome_message(bot.get_me()),
        parse_mode="Markdown")
    #envía lista de comandos 
    bot.send_message(
        message.chat.id,
        logic.get_help_message(),
        parse_mode="Markdown")
    
    
    markup =   types.ReplyKeyboardMarkup(one_time_keyboard=True)
    bot.send_message(message.chat.id, "Eres nuevo usuario?:",
        reply_markup=markup)
    itembtn1 = types.KeyboardButton('/si')
    itembtn2 = types.KeyboardButton('/no')

    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id, "Selecciona una opción del menú:",
        reply_markup=markup)

#########################################################

@bot.message_handler(commands=['si'])
def registro_usuario(due_documento,due_nombre, due_tipo_usuario):
    ### Registro de usuario
    usuario =  bd.session.query(Dueno).filter(and_(Dueno.due_documento == due_documento, Dueno.due_tipo_usuario == due_tipo_usuario)).first()
    bd.session.commit() 
    
    if usuario == None:
            usuario = Duenos(
                due_documento, 
                due_nombre, 
                due_tipo_usuario)
            bd.session.add(usuario)
            bd.session.commit()
            return True
    return False
        


#HELP
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_help_message(),
        parse_mode="Markdown") 

#########################################################

#ABOUT
@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        logic.get_about_this(config.VERSION),
        parse_mode="Markdown")

#########################################################
#FALLBACK
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    response = logic.get_fallback_message(message.text)
    bot.reply_to(message, response)

#########################################################

if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################
