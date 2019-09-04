
# A very simple Flask Hello World app for you to get started with...

from flask import *
import sqlite3
from sqlite3 import Error
from process import  check_login

app = Flask(__name__)
#mohit edit
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
# set FLASK_DEBUG=1
# on cmd
#end mohit edit

@app.route('/')
def home():
    if session.get('logged_in'):
        return 'welcome user '+session.get('user_email')
    return 'Hello from Flask!'

@app.route('/login',  methods=['GET', 'POST'])
# imp to write methods
def login():
    error=' '
    if request.method=="POST":
        ans=check_login(request.form['email'],request.form['password'])
        if ans:
            session['logged_in']=True
            session['user_email']=request.form['email']
            return '''login successful'''
        else:
            error='wrong details'

    #flash('hi')
    return render_template('login.html', errors=error)

@app.route('/logout')
def logout():
    session['logged_in']=False
    session['user_email']=None
    return ''' logged out ... see you soon! '''
