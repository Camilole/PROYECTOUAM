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
global nombre
diccionario = {}
class General_information():
    def __init__(self, nombre = None, cargo = None, usuario_id = None, tipo = None):
        self.nombre = nombre
        self.cargo = cargo
        self.usuario_id = usuario_id
        self.tipo = tipo
        

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.nombre, self.cargo, self.usuario_id, self.tipo)

#########################################################
info = General_information()

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
    response1 = bot.reply_to(message, "Ingresa tu nombre de usuario")
    bot.register_next_step_handler(response1, proceso_tipo_usuario)

@bot.message_handler(commands=['No'])
def on_command_imc(message):
    response3 = bot.reply_to(message, "Ingresa el nombre de usuario ya registrado")
    bot.register_next_step_handler(response3, proceso_cargar_usuario)

def proceso_tipo_usuario(message):
    try:
        nombre = message.text
        info.nombre = nombre
        print(nombre)
        response2 = bot.reply_to(message, 'escribe tipo de usuario Dueño de Empresa - Dueño de Vehiculo - Mecanico')
        print(response2.text)
        bot.register_next_step_handler(response2, proceso_registrar_usuario)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")
    
def proceso_registrar_usuario(message):
    try:
        cargo = message.text
        info.cargo = cargo
        record = message.chat.id
        info.usuario_id = record
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usu_codigo, usu_nombre, usu_tipo) VALUES (?, ?, ?)", (info.usuario_id, info.nombre, info.cargo))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"Usuario creado satisfactoriamente, usted ya puede comenzar a utilizar nuestros servicios")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

def proceso_cargar_usuario(message):
    try:
        cargar_usuario = message.text
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("SELECT usu_codigo, usu_nombre, usu_tipo FROM usuarios")
        results = cursor.fetchall()
        response = ""
        for row in results:
            response += f"Codigo de usuario: {row[0]}, Nombre del Usuario: {row[1]}, Tipo de Usuario: {row[2]}\n"

        # Send the response to the user
        bot.reply_to(message, response)
        conn.commit()
        conn.close()
        bot.reply_to(message, f"su usuario a sido cargado")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

@bot.message_handler(commands=['vehiculo'])
def on_command_imc(message):
    response4 = bot.reply_to(message, "Modulo de registro de vehiculo, ingrese el tipo de vehiculo Microbús o Busetas")
    bot.register_next_step_handler(response4, proceso_registrar_ano)
    
def proceso_registrar_ano(message):
    try:
        tipo = message.text
        info.tipo = tipo
        response5 = bot.reply_to(message, 'Ingrese el Año del Vehiculo')
        bot.register_next_step_handler(response5, proceso_registrar_vehiculo)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")    

def proceso_registrar_vehiculo(message):
    try:
        veh_codigo = '1'
        ano = message.text
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vehiculos (veh_codigo, veh_tipo, veh_ano) VALUES (?, ?, ?)", (veh_codigo, info.tipo, ano))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"Vehiculo creado satisfactoriamente")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")    
         
    
def proceso_registrar_ano(message):
    try:
        tipo = message.text
        info.tipo = tipo
        response5 = bot.reply_to(message, 'Ingrese el Año del Vehiculo')
        bot.register_next_step_handler(response5, proceso_registrar_vehiculo)
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}") 
        
@bot.message_handler(commands=['rvehiculo'])
def on_command_imc(message):
        response6 = bot.reply_to(message, "Ingrese el tipo de vehiculo")
        bot.register_next_step_handler(response6, proceso_cargar_vehiculo)

def proceso_cargar_vehiculo(message):
    try:
        cargar_vehiculo = message.text
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("SELECT veh_codigo, veh_tipo, veh_ano FROM vehiculos")
        results = cursor.fetchall()
        response = ""
        for row in results:
            response += f"Codigo de vehiculo: {row[0]}, Tipo del Vehiculo: {row[1]}, Año del Vehiculo: {row[2]}\n"

        # Send the response to the user
        bot.reply_to(message, response)
        conn.commit()
        conn.close()
        bot.reply_to(message, f"su Vehiculo a sido cargado")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")

@bot.message_handler(commands=['repuestos'])
def on_command_imc(message):
        response7 = bot.reply_to(message, "Ingrese el el repuesto a registrar")
        bot.register_next_step_handler(response7, proceso_registrar_repuesto)
        
def proceso_registrar_repuesto(message):
    try:
        rep_codigo = '1'
        rep_nombre = message.text
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO repuestos (rep_codigo, veh_nombre) VALUES (?, ?)", (rep_codigo, rep_nombre))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"Repuesto creado satisfactoriamente")
    except Exception as e:
        bot.reply_to(message, f"Algo terrible sucedió: {e}")   

@bot.message_handler(commands=['rrepuestos'])
def on_command_imc(message):
        response6 = bot.reply_to(message, "Ingrese el nombre del repuesto")
        bot.register_next_step_handler(response6, proceso_cargar_repuestos)

def proceso_cargar_repuestos(message):
    try:
        cargar_repuestos = message.text
        conn = sqlite3.connect('control_service.db')
        cursor = conn.cursor()
        cursor.execute("SELECT rep_codigo, veh_nombre FROM repuestos")
        results = cursor.fetchall()
        response = ""
        for row in results:
            response += f"Codigo del repuesto: {row[0]}, Nombre del repuesto: {row[1]}\n"

        # Send the response to the user
        bot.reply_to(message, response)
        conn.commit()
        conn.close()
        bot.reply_to(message, f"su repuesto a sido cargado")
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