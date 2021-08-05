from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('sleeptracker.html')

@main.route('/boostyourself')
def boost():
    return render_template('boostyourself.html')
    