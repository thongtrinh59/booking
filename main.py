from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Resource, Api
from flask_restx import fields
from flask_restx import inputs
from flask_restx import reqparse
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import copy


import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://root:root@dbbooking/main'

db = SQLAlchemy(app)
engine = create_engine('postgresql://root:root@dbbooking/main')
Session = sessionmaker(bind = engine)
session = Session()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))

    
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    ticketid = db.Column(db.Integer)
    


@app.before_first_request
def create_tables():
    print("---------------------------------------")
    db.create_all()
    db.session.commit()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
