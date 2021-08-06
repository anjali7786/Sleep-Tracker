from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__ , template_folder= 'Template' , static_folder='Static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/records'
db = SQLAlchemy(app)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)

class Day(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    bed = db.Column(db.DateTime, unique=False, nullable=True)
    wake = db.Column(db.DateTime, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def home():
    return render_template('sleeptracker.html')

@app.route("/Trackmysleep")
def track_your_sleep():
    return render_template('Trackmysleep.html')

@app.route("/records", methods = ['GET', 'POST'])
def records():
    if (request.method == 'POST'):
        bed_t = request.form.get('bed')
        wake_t = request.form.get('wake')

        entry = Day(bed = bed_t, wake = wake_t)
        db.session.add(entry)
        db.session.commit()

    return render_template('records.html')

# @app.route("/login")
# def login():
#     return render_template('login.html')

# @app.route("/signup", methods=["GET","POST"])
# def signup():
#     if(request.method =='POST'):
#         name = request.form.get('name')
#         age = request.form.get('age')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         cpassword = request.form.get('cpassword')

#         if(password==cpassword):
#             entry = login(name=name , age=age ,email=email , password=password)
#             db.session.add(entry)
#             db.session.commit()
#             return render_template('sleeptracker.html')
            
#         else:
#             return("incorrect password! please try again.")
            
#     return render_template('signup.html')


@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM login WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('sleeptracker.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/signup', methods =['GET', 'POST'])
def signup():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM login WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO login VALUES (NULL, % s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('signup.html', msg = msg)



@app.route("/unabletosleep")
def unable_to_sleep():
    return render_template('unabletosleep.html')

@app.route("/unabletosleep/yoga")
def yoga():
    return render_template('yoga.html')

@app.route("/boostyourself")
def boost_yourself():
    return render_template('boostyourself.html')

app.run(debug=True)