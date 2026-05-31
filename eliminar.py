# ===============================
# ELIMINAR USUARIO
# ===============================

import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("usuarios.db")

# Crear cursor
cursor = conexion.cursor()

# Pedir ID a eliminar
id_usuario = int(input("ID del usuario a eliminar: "))

# Ejecutar DELETE
cursor.execute(
    "DELETE FROM usuarios WHERE id = ?",
    (id_usuario,)
)

# Guardar cambios
conexion.commit()

print("✅ Usuario eliminado")

# Cerrar conexión
conexion.close()