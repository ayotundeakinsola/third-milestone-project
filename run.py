import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'mysecret'

app.config["MONGO_DBNAME"] = 'recruitment'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-qowfo.mongodb.net/recruitment?retryWrites=true&w=majority'

mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user):
    return users.get(user)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=80)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember_me = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



@app.route('/')
def index():
    return render_template("index.html", title='Home')

@app.route('/about')
def about():
    return render_template("about.html", title='About')


@app.route('/candidate')
def candidate():
    return render_template("candidate.html", title='Candidate')

@app.route('/employers')
def employers():
    return render_template("employers.html", employ=mongo.db.employer.find(), title='Employers')

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')

@app.route('/employer_form', methods=['GET', 'POST'])
def employer_form():
    if request.method == 'POST':
        employ = mongo.db.employer
        employ.insert_one(request.form.to_dict())
    return render_template('employerform.html', title='Submit your vacancy', employ=mongo.db.employer.find())

@app.route('/vacancies')
def vacancies():
    return render_template("vacancy.html", title='Vacancy')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
         # Create collection to store all the usernames and passwords
        user = mongo.db.users.find_one({'username' : request.form.get['username']})
        if user is None or not user.check_password_hash(request.form.get['password']):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=request.form['remember_me'])
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)
    
@app.route('/logout')
def logout():
    flash("You have been logged out")
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(request.form['password'], method='sha256')
        existing_user = mongo.db.users.insert({'username' : request.form['username'], 'email' : request.form['email'],'password' : hashed_password})
        session['username'] = request.form['username']
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
