# ===============================
# ACTUALIZAR USUARIO
# ===============================

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("usuarios.db")

# Crear cursor
cursor = conexion.cursor()

# Pedir datos
id_usuario = int(input("ID del usuario a actualizar: "))
nuevo_nombre = input("Nuevo nombre: ")
nueva_edad = int(input("Nueva edad: "))

# Ejecutar UPDATE
cursor.execute("""
UPDATE usuarios
SET nombre = ?, edad = ?
WHERE id = ?
""", (nuevo_nombre, nueva_edad, id_usuario))

# Guardar cambios
conexion.commit()

print("✅ Usuario actualizado")

# Cerrar conexión
conexion.close()