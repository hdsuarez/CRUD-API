# ===============================
# CONSULTAR USUARIOS
# ===============================

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("usuarios.db")

# Crear cursor
cursor = conexion.cursor()

# Consultar todos los usuarios
cursor.execute("SELECT * FROM usuarios")

# Obtener resultados
usuarios = cursor.fetchall()

print("\n📋 LISTA DE USUARIOS:\n")

# Recorrer resultados
for usuario in usuarios:

    print(usuario)

# Cerrar conexión
conexion.close()