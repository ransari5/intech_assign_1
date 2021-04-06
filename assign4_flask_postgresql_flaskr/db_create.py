#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member
"""
this is a database file
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yuva09@localhost/startup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project(db.Model):
   __tablename__ = 'project'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   desc = db.Column(db.String(100))
   sol = db.Column(db.String(100))


   def __init__(self, id, name, desc, sol):
      
      self.id = id
      self.name = name
      self.desc = desc
      self.sol = sol


if __name__ == '__main__':
	app.run(debug = True)