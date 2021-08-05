from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
# from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__ , template_folder= 'Template' , static_folder='Static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/records'
db = SQLAlchemy(app)


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