import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
         # Check first if user already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
       
        if existing_user:
            flash("Username already exists! Please try again.")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
            }
        mongo.db.users.insert_one(register)

        #Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("index"))
    return render_template('register.html', title='Register')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method== 'POST':
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username' : request.form.get('username').lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        session['logged_in'] = True
                        flash("Welcome {}".format(request.form.get("username")))
                        return redirect(url_for("index"))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))
        
        else:
                #username doesn't exist
                flash("Incorrect Username and/or Password!")
                return redirect(url_for("login"))
    
    return render_template("login.html", title='Login')
    
@app.route('/logout')
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user", None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
