#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member
"""
this is a database file
"""

from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yuva09@localhost:5432/startup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecretkey'
db = SQLAlchemy(app)

class Register(db.Model):
   __tablename__ = 'register'
   id = db.Column(db.Integer, primary_key = True)
   fname = db.Column(db.String(100))
   lname = db.Column(db.String(100))
   mail = db.Column(db.String(100), unique = True)
   pwd = db.Column(db.String(100))
   cpwd = db.Column(db.String(100))

class Login(db.Model):
   __tablename__ = 'login'
   id = db.Column(db.Integer, primary_key = True)
   mail = db.Column(db.String(100), unique = True)
   pwd = db.Column(db.String(100))

class Project(db.Model):
   __tablename__ = 'project'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   desc = db.Column(db.String(100))
   sol = db.Column(db.String(100))


@app.route('/', methods = ["POST", "GET"])  
def title():
   return render_template('register.html')

@app.route('/', methods = ['POST', 'GET'])

def register():
   if request.method == "POST":
      id = request.form['id']
      fname = request.form['fname']
      lname = request.form['lname']
      mail = request.form['mail']
      pwd = request.form['pwd']
      cpwd = request.form['cpwd']
      user = Register(id = id, fname = fname, lname = lname, mail = mail, pwd = pwd, cpwd = cpwd)
      db.session.add(user)
      db.session.commit()
      return render_template('login.html', user=user)

   return render_template('register.html') 



@app.route('/login.html', methods = ['POST', 'GET'])  
def login():
   if request.method == "POST":
      id = request.form['id']
      mail = request.form['mail']
      pwd = request.form['pwd']
      log = Login(id = id, mail = mail, pwd = pwd)
      db.session.add(log)
      db.session.commit()
      return render_template('create.html', user=log)
   return render_template('login.html')


@app.route('/create.html', methods = ['POST', 'GET'])  
def create():
   return render_template('create.html')


@app.route('/details.html', methods = ['POST', 'GET'])  
def details():
   if request.method == "POST":
      id = request.form['id']
      name = request.form['name']
      desc = request.form['desc']
      sol = request.form['sol']
      obj = Project(id = id, name = name, desc = desc, sol = sol)
      db.session.add(obj)
      db.session.commit()
      return render_template('end.html', user=obj)

   return render_template('details.html')
  
if __name__ =="__main__":  
    app.run(debug = True)  