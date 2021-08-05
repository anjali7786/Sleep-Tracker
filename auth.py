# from flask import Blueprint, render_template
# from flask.helpers import url_for
# from werkzeug.utils import redirect

# auth = Blueprint('auth', __name__)

# @auth.route('/login')
# def login():
#     return render_template('login.html')

# # @auth.route('/login', methods = ['POST'])
# # def login_post():

# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')

# # @auth.route('/signup', methods = ['POST'])
# # def signup_post():

# @auth.route('/logout')
# def logout():
#     return redirect(url_for('main.home'))
