from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os, uuid
from werkzeug.utils import secure_filename
from datetime import date, timedelta, datetime

app = Flask(__name__)

app.secret_key='#the#secret#key#'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'tracknap'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:
        return render_template('sleeptracker.html', username=session['username'],
                               email1=session['email1'])
    return render_template('index.html',username="",email1="")

@app.route("/login", methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) > 0 and len(password) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM login WHERE username = %s', (username, ))
            user = cursor.fetchone()
            mysql.connection.commit()
            cursor.close()
            if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                    session['loggedin'] = True
                    session['id'] = user['id']
                    session['username'] = user['username']
                    session['age'] = user['age']
                    session['email'] = user['email']
                    session['mobile'] = user['mobile']
                    return redirect(url_for('sleeptracker'))
            else:
                msg = 'Incorrect username/password!'
        else:
            msg = ' Please fill the form !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('age', None)
    session.pop('mobile', None)
    return redirect(url_for('login'))


@app.route("/signup", methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']
        mobile = request.form['mobile']
        cpassword = request.form['cpassword']
        if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(mobile) > 0 and len(fullname) > 0 and len(
                cpassword) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
            account = cursor.fetchone()
            cursor.execute('SELECT * FROM accounts WHERE email = % s', (email,))
            account1 = cursor.fetchone()
            cursor.execute('SELECT * FROM accounts WHERE mobile = % s', (mobile,))
            account2 = cursor.fetchone()
            if account:
                msg = 'Account already exists with this username!'
            elif account1:
                msg = 'Account already exists with this email !'
            elif account2:
                msg = 'Account already exists with this mobile number !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password or not email or not mobile or not cpassword or not fullname:
                msg = 'Please fill out the form !'
            elif len(mobile) != 10:
                msg = 'Enter 10 digit number !'
            elif cpassword != password:
                msg = "Password doesn't match!"
            else:
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s,% s,% s,% s)',
                               (username, fullname, age , email, mobile, hashed,))
                mysql.connection.commit()
                cursor.close()
                msg = 'You have successfully Signed In !'
        else:
            msg = 'Please fill out the form !'

    return render_template('signup.html', msg=msg)


