from config import *
import telebot
import sqlite3

#Comenzar conexion a la Base de Datos

conn = sqlite3.connect('control_service.db')
cursor = conn.cursor()

#crear Tabla Usuarios
crear_usuarios = """CREATE TABLE IF NOT EXISTS usuarios (
    usu_codigo INTEGER PRIMARY KEY,
    usu_nombre TEXT,
    usu_tipo TEXT)"""

cursor.execute(crear_usuarios)

# crear Tabla Vehiculos
crear_vehiculos = """CREATE TABLE IF NOT EXISTS vehiculos (
    veh_codigo TEXT PRIMARY KEY,
    veh_tipo TEXT,
    veh_ano TEXT)"""
    
cursor.execute(crear_vehiculos)

# crear tabla Repuestos
crear_repuestos = """CREATE TABLE IF NOT EXISTS repuestos (
    rep_codigo INTEGER PRIMARY KEY,
    veh_nombre TEXT)"""
    
cursor.execute(crear_repuestos)

# crear Tabla seguros
crear_seguros = """CREATE TABLE IF NOT EXISTS seguros (
    seg_codigo TEXT PRIMARY KEY,
    seg_tipo TEXT,
    seg_fecha_expedicion DATE,
    veh_codigo TEXT,
    FOREIGN KEY(veh_codigo) REFERENCES vehiculos(veh_codigo))"""
    
cursor.execute(crear_seguros)

# crear Tabla servicios
crear_servicios = """CREATE TABLE IF NOT EXISTS servicios (
    ser_codigo INT PRIMARY KEY,
    veh_codigo TEXT,
    ser_motor TEXT,
    ser_transmision TEXT,
    ser_frenos TEXT,
    ser_refrijerante TEXT,
    ser_direccion TEXT,
    ser_fecha DATE,
    usu_codigo_dueno INTERGER,
    usu_codigo_mecanico INTERGER,
    FOREIGN KEY(usu_codigo_dueno) REFERENCES usuarios(usu_codigo),
    FOREIGN KEY(usu_codigo_mecanico) REFERENCES usuarios(usu_codigo),
    FOREIGN KEY(veh_codigo) REFERENCES vehiculos(veh_codigo))"""
    
cursor.execute(crear_servicios)

conn.close()
