from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configurar la conexión a la base de datos
db_config = {
    'host': 'aws.connect.psdb.cloud',
    'user': 'vday78i50d4mb8bb2dn2',
    'password': 'pscale_pw_FJkxXAqMFPlCf0leqx6pCXZ9L4LfEi3SXYcRSshidoZ',
    'database': 'lab11'
}

# Ruta principal
@app.route('/', methods=['GET'])
def index():
    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Obtener los registros de la tabla 'books'
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    # Renderizar el template 'index.html' con los registros obtenidos
    return render_template('index.html', rows=rows)

# Ruta para agregar un libro
@app.route('/add', methods=['POST'])
def add():
    # Obtener los datos del formulario
    title = request.form['title']
    author = request.form['author']

    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insertar el libro en la tabla 'books'
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    # Redirigir a la página principal
    return redirect(url_for('index'))

# Ruta para eliminar un libro
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Eliminar el libro de la tabla 'books'
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    conn.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    # Redirigir a la página principal
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
