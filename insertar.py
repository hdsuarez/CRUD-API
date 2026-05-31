# ===============================
# INSERTAR USUARIO
# ===============================

import sqlite3

# Conectarse a la base de datos
conexion = sqlite3.connect("usuarios.db")

# Crear cursor
cursor = conexion.cursor()

# -------------------------------
# PEDIR DATOS AL USUARIO
# -------------------------------

nombre = input("Nombre: ")
edad = int(input("Edad: "))

# -------------------------------
# INSERTAR EN SQLITE
# -------------------------------

cursor.execute("""
INSERT INTO usuarios (nombre, edad)
VALUES (?, ?)
""", (nombre, edad))

# Guardar cambios
conexion.commit()

print("✅ Usuario agregado")

# Cerrar conexión
conexion.close()