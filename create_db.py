import sqlite3 # Era sqlite3, no splite3

# Conectamos (esto crea el archivo users.db si no existe)
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Corregimos los errores de sintaxis SQL:
# KEY en lugar de HEY, AUTOINCREMENT bien escrito, TEXT en lugar de TET
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        password TEXT NOT NULL
    )
''')  

connection.commit()
connection.close()
print('Base de datos creada exitosamente.')