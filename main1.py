from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__ , template_folder= 'Template' , static_folder='Static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/records'
# db = SQLAlchemy(app)


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

@app.route("/signup")
def signup():
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