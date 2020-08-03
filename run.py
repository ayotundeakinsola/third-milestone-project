import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

# ---- CONFIG ----- #

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')

mongo = PyMongo(app)

# ---- Home Page ----- #
@app.route('/')
def index():
    return render_template("index.html", title='Home')

# ---- About Page ----- #
@app.route('/about')
def about():
    return render_template("about.html", title='About')

# ---- Employers Page ----- #
@app.route('/employers')
def employers():
    return render_template("employers.html", title='Employers')

# ---- Contact Page ----- #
@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')

# ---- Vacancies Page ----- #
@app.route('/vacancies')
def vacancies():
    return render_template("vacancy.html", title='Vacancy', employ=mongo.db.employer.find())

# ---- Listing Page ----- #
@app.route('/listing/<employer_id>')
def listing(employer_id):
    the_list =  mongo.db.employer.find_one({"_id": ObjectId(employer_id)})
    return render_template('listing.html', employer=the_list, title='Listing')

# ---- Employer_form Page ----- #
@app.route('/employer_form', methods=['GET', 'POST'])
def employer_form():
    if request.method == 'POST':
        employ = mongo.db.employer
        employ.insert_one(request.form.to_dict())
        flash("Your vacancy has been received!")
        return redirect(url_for("vacancies"))
    return render_template('employerform.html', title='Post A Job')

# ---- Edit_job Page ----- #
@app.route('/edit_job/<employer_id>')
def edit_job(employer_id):
    the_job =  mongo.db.employer.find_one({"_id": ObjectId(employer_id)})
    return render_template('editemployerform.html', employer=the_job, title='Edit A Job')


# ---- Update a Job----- #
@app.route('/update_job/<employer_id>', methods=['POST'])
def update_job(employer_id):
    employ = mongo.db.employer
    employ.update( {'_id': ObjectId(employer_id)},
    {
        'salutation':request.form.get('salutation'),
        'first_name':request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'company_name': request.form.get('company_name'),
        'size':request.form.get('size'),
        'employment': request.form.get('employment'),
        'salary': request.form.get('salary'),
        'email':request.form.get('email'),
        'address':request.form.get('address'),
        'phone': request.form.get('phone'),
        'job': request.form.get('job')
    })
    return redirect(url_for('vacancies'))

# ---- Delete a Job ----- #
@app.route('/delete_job/<employer_id>')
def delete_job(employer_id):
    mongo.db.employer.remove({'_id': ObjectId(employer_id)})
    flash("Your vacancy has been deleted!")
    return redirect(url_for('vacancies'))

# ---- Candidate form Page ----- #
@app.route('/candidate_form', methods=['GET', 'POST'])
def candidate_form():
    if request.method == 'POST':
        candidate = mongo.db.candidates
        candidate.insert_one(request.form.to_dict())
        flash("Your application has been received!")
        return redirect(url_for("index"))
    return render_template('candidateform.html', title='Submit Your Vacancy', candidate=mongo.db.candidates.find())

# ---- Contact Us Form ----- #
@app.route('/contactus_form', methods=['GET', 'POST'])
def contactus_form():
    if request.method == 'POST':
        contact = mongo.db.contacts
        contact.insert_one(request.form.to_dict())
        flash("We would be in contact with you!")
        return redirect(url_for("index"))
    return render_template('contact.html', title='Contact', contact=mongo.db.contacts.find())

# ---- Sign up Page ----- #
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
        flash("Registration Successful!")
        return redirect(url_for("index"))
    return render_template('register.html', title='Register')

# ---- Login Page ----- #
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

# ---- Logout Page ----- #    
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
