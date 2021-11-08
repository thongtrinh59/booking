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

# create booking template
@app.route('/test/<cinemaname>')
def get_info_cinema(cinemaname):

    with engine.connect() as con:
        q_str = "SELECT * FROM cinema;"
        rs = con.execute(q_str)
        for _ in rs:
            print(_)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
