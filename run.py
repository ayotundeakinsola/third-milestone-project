import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)


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
    return render_template("employers.html", title='Employers')

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
