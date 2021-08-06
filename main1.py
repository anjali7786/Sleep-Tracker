from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__ , template_folder= 'Template' , static_folder='Static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tracknap'
db = SQLAlchemy(app)

class Login(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(25), nullable=False)



# class Day(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     bed = db.Column(db.String(80), unique=False, nullable=False)
#     wake = db.Column(db.String(120), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

@app.route("/")
def home():
    return render_template('sleeptracker.html')

@app.route("/Trackmysleep")
def track_your_sleep():
    return render_template('Trackmysleep.html')

@app.route("/records")
def records():
    return render_template('records.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup", methods=["GET","POST"])
def signup():
    if(request.method =='POST'):
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        if(password==cpassword):
            entry = Login(name=name , age=age ,email=email , password=password)
            db.session.add(entry)
            db.session.commit()
            return render_template('sleeptracker.html')
            
        else:
            return("incorrect password! please try again.")
            
    return render_template('signup.html')

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