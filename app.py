from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = ' just anything'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mayankm698'
app.config['MYSQL_DB'] = 'form_db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    msg = 'error home cannot be loaded'
    return render_template('index.html', msg= msg)

@app.route('/form', methods=['GET', 'POST'])
def form():
    msg = ''
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM form WHERE username = %s', (username,))
        form_details = cursor.fetchone()
        if form_details:
            msg = 'Details already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO form VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'form submitted successfully!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('form.html', msg=msg)

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    msg =''
    return render_template('chart.html', msg=msg)

