# ===============================
# CRUD API CON FASTAPI
# ===============================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
# Crear aplicación
app = FastAPI()

#conexion sqlite base de dats

def obtener_conexion():

    conexion = sqlite3.connect("usuarios.db")

    return conexion

# ===================================
# CONFIGURACIÓN CORS
# ===================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# BASE DE DATOS FAKE
# ===============================

usuarios = [

    {
        "id": 1,
        "nombre": "Hector",
        "edad": 30
    },

    {
        "id": 2,
        "nombre": "Maria",
        "edad": 25
    },

    {
        "id": 3,
        "nombre": "Ramiro",
        "edad": 35
    }

]

# ===============================
# READ → VER USUARIOS
# ===============================

@app.get("/usuarios")
def obtener_usuarios():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")

    datos = cursor.fetchall()

    conexion.close()

    return datos

# ===============================
# CREATE → CREAR USUARIO
# ===============================
@app.post("/crear/{nombre}/{edad}")

def crear_usuario(nombre: str, edad: int):

    # Conectar a SQLite
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    # Insertar usuario
    cursor.execute("""
    INSERT INTO usuarios (nombre, edad)
    VALUES (?, ?)
    """, (nombre, edad))

    # Guardar cambios
    conexion.commit()

    # Obtener el ID generado automáticamente
    nuevo_id = cursor.lastrowid

    conexion.close()

    return {

        "mensaje": "Usuario creado ✅",

        "usuario": {
            "id": nuevo_id,
            "nombre": nombre,
            "edad": edad
        }

    }
# ===============================
# UPDATE → ACTUALIZAR USUARIO
# ===============================

@app.put("/actualizar/{id}/{nuevo_nombre}/{nueva_edad}")

def actualizar_usuario(id: int, nuevo_nombre: str, nueva_edad: int):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET nombre = ?, edad = ?
    WHERE id = ?
    """, (nuevo_nombre, nueva_edad, id))

    conexion.commit()

    conexion.close()

    return {

        "mensaje": "Usuario actualizado 🔄",

        "usuario": {
            "id": id,
            "nombre": nuevo_nombre,
            "edad": nueva_edad
        }

    }

# ===============================
# DELETE → ELIMINAR USUARIO
# ===============================

@app.delete("/eliminar/{id}")

def eliminar_usuario(id: int):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE id = ?
    """, (id,))

    conexion.commit()

    conexion.close()

    return {

        "mensaje": "Usuario eliminado ❌",
        "id": id

    }