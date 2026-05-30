# ===============================
# CRUD API CON FASTAPI
# ===============================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crear aplicación
app = FastAPI()

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

    return usuarios

# ===============================
# CREATE → CREAR USUARIO
# ===============================

@app.post("/crear/{nombre}")

def crear_usuario(nombre: str):

    nuevo_usuario = {

        "id": len(usuarios) + 1,
        "nombre": nombre

    }

    usuarios.append(nuevo_usuario)

    return {

        "mensaje": "Usuario creado ✅",
        "usuario": nuevo_usuario

    }

# ===============================
# UPDATE → ACTUALIZAR USUARIO
# ===============================

@app.put("/actualizar/{id}/{nuevo_nombre}")

def actualizar_usuario(id: int, nuevo_nombre: str):

    for usuario in usuarios:

        if usuario["id"] == id:

            usuario["nombre"] = nuevo_nombre

            return {

                "mensaje": "Usuario actualizado 🔄",
                "usuario": usuario

            }

    return {

        "error": "Usuario no encontrado"

    }

# ===============================
# DELETE → ELIMINAR USUARIO
# ===============================

@app.delete("/eliminar/{id}")

def eliminar_usuario(id: int):

    for usuario in usuarios:

        if usuario["id"] == id:

            usuarios.remove(usuario)

            return {

                "mensaje": "Usuario eliminado ❌"

            }

    return {

        "error": "Usuario no encontrado"

    }