from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os, uuid
from werkzeug.utils import secure_filename
from datetime import date, timedelta, datetime

app = Flask(__name__, template_folder= 'Template' , static_folder='Static')

app.secret_key='#the#secret#key#'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tracknap'

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def sleeptracker():
    if 'loggedin' in session:
        return render_template('sleeptracker.html', username=session['username'],
                               email1=session['email'])
    return render_template('sleeptracker.html',username="",email="")

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
                    # session['fullname'] = user['fullname']
                    session['username'] = user['username']
                    # session['age'] = user['age']
                    session['email'] = user['email']
                    # session['mobile'] = user['mobile']
                    return redirect(url_for('sleeptracker'))
            else:
                msg = "Incorrect username/password!"
        else:
            msg = " Please fill the form !"
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email', None)
    # session.pop('age', None)
    # session.pop('mobile', None)
    return redirect(url_for('login'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # age = request.form['age']
        # mobile = request.form['mobile']
        cpassword = request.form['cpassword']
        if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(fullname) > 0 and len(
                cpassword) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM login WHERE username = % s', (username,))
            account = cursor.fetchone()
            cursor.execute('SELECT * FROM login WHERE email = % s', (email,))
            account1 = cursor.fetchone()
            # cursor.execute('SELECT * FROM accounts WHERE mobile = % s', (mobile,))
            # account2 = cursor.fetchone()
            if account:
                msg = 'Account already exists with this username!'
            elif account1:
                msg = 'Account already exists with this email !'
            # elif account2:
            #     msg = 'Account already exists with this mobile number !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password or not email or not cpassword or not fullname:
                msg = 'Please fill out the form !'
            # elif len(mobile) != 10:
            #     msg = 'Enter 10 digit number !'
            elif cpassword != password:
                msg = "Password doesn't match!"
            else:
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute('INSERT INTO login VALUES (NULL, % s, % s, % s,% s, % s)',(fullname, username , email, hashed, hashed,))
                mysql.connection.commit()
                cursor.close()
                msg = 'You have successfully Signed In !'
        else:
            msg = 'Please fill out the form !'

    return render_template('signup.html', msg=msg)

    
# @app.route("/")
# def home():
#     return render_template('sleeptracker.html')

@app.route("/Trackmysleep")
def track_your_sleep():
    return render_template('Trackmysleep.html')

@app.route("/records", methods = ['GET', 'POST'])
def records():
     if (request.method == 'POST'):
        bed1 = request.form('bed1')
        wake1 = request.form('wake1')
        bed2 = request.form('bed2')
        wake2 = request.form('wake2')
        bed3 = request.form('bed3')
        wake3 = request.form('wake3')
        bed4 = request.form('bed4')
        wake4 = request.form('wake4')
        bedt1 = request.form('bedt1')
        waket1 = request.form('waket1')
        bedt2 = request.form('bedt2')
        waket2 = request.form('waket2')
        bedt3 = request.form('bedt3')
        waket3 = request.form('waket3')
        bedt4 = request.form('bedt4')
        waket4 = request.form('waket4')
        

        if len(bed1) > 0 and len(wake1) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bed1, wake1,date.now(),))
        
        if len(bed2) > 0 and len(wake2) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bed2, wake2,date.now(),))
        
        if len(bed3) > 0 and len(wake3) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bed3, wake3,date.now(),))
        
        if len(bed4) > 0 and len(wake4) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bed4, wake4,date.now(),))
        
        if len(bedt1) > 0 and len(waket1) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bedt1, waket1,date.now(),))
        
        if len(bedt2) > 0 and len(waket2) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bedt2, waket2,date.now(),))
        
        
        if len(bedt3) > 0 and len(waket3) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bedt3, waket3,date.now(),))

        if len(bedt4) > 0 and len(waket4) > 0 :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            cursor.execute('INSERT INTO records VALUES (NULL, % s, % s, % s,% s)',( session['username'] ,session['email'] , bedt4, waket4,date.now(),))

     return render_template('records.html')

@app.route("/unabletosleep")
def unable_to_sleep():
    return render_template('unabletosleep.html')

@app.route("/boostyourself")
def boost_yourself():
    return render_template('boostyourself.html')

app.run(debug=True)    

