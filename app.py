from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. RUTA RAÍZ (Te manda al Login por defecto)
@app.route('/')
def index():
    return redirect(url_for('login'))

# 2. RUTA DE INICIO (A donde llegas al entrar con éxito)
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# 3. RUTA DE REGISTRO
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('username')
        clave = request.form.get('password')
        
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        try:
            # Guardamos al usuario en la base de datos
            cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (nombre, clave))
            conn.commit()
            # IMPORTANTE: Después de registrarse, lo mandamos al inicio directamente
            return redirect(url_for('inicio'))
        except sqlite3.IntegrityError:
            return "<h1>El usuario ya existe</h1><a href='/register'>Intentar de nuevo</a>"
        finally:
            conn.close()
            
    return render_template('register.html')

# 4. RUTA DE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('username')
        clave = request.form.get('password')
        
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Buscamos si las credenciales coinciden
        cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (nombre, clave))
        user = cursor.fetchone()
        conn.close()

        if user:
            # REDIRECCIÓN CORRECTA: 'inicio' es el nombre de la función arriba
            return redirect(url_for('inicio'))
        else:
            return "<h1>Usuario o contraseña incorrectos</h1><a href='/login'>Volver a intentar</a>"
            
    return render_template('home.html')

# 5. EJECUCIÓN
if __name__ == '__main__':
    app.run(debug=True)