# ===============================
# SQLITE BÁSICO
# ===============================

import sqlite3

# Crear conexión
conexion = sqlite3.connect("usuarios.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER

)
""")

# Guardar cambios
conexion.commit()

print("✅ Base de datos creada")