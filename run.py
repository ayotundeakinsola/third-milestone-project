import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
