import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'mysecret'

app.config["MONGO_DBNAME"] = 'recruitment'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-qowfo.mongodb.net/recruitment?retryWrites=true&w=majority'

mongo = PyMongo(app)

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
    if request.method== 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['email']})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode ('utf-8'), login_user['password']) == login_user['password']:
                session['email'] = request.form['email']
                return redirect(url_for('index'))

        return 'Invalid email/password combination'
    
    return render_template("login.html", title='Login')
    
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You were just logged out')
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method== 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode ('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['email'], 'password':hashpass})
            session['email'] = request.form['email']
            return redirect(url_for('login'))

        return 'That email already exists!'

    return render_template("register.html", title='Register')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
