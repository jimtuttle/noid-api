#!/usr/bin/env python3

import os
from flask import Flask, jsonify, abort, make_response, request
from flask_marshmallow import Marshmallow
from string import ascii_lowercase, digits
from random import SystemRandom
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from pymysql import cursors

app = Flask(__name__)

dbhost = 'localhost'
dbport = '3306'
dbname = 'noid'
dbuser = os.environ['NOID_DB_USER']
dbpassword = os.environ['NOID_DB_PASSWORD']
db_connect_string = "{}:{}@{}:{}/{}".format(dbuser, dbpassword, dbhost, dbport, dbname)
Base = declarative_base()
engine = create_engine('mysql+pymysql://{}'.format(db_connect_string), pool_recycle=3600,
                       isolation_level='READ UNCOMMITTED')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    token = Column(String)

    def __repr__(self):
        return "<User(username='%s', email='%s', id = '%s')>" % (self.username, self.email, self.user_id)

    def get_user_profile(username):
        for user in session.query(User).filter_by(username='jjtuttle'):
            return user


class Noid(Base):
    __tablename__ = 'noid'
    user_id = Column(Integer, primary_key=True)
    identifier = Column(String, unique=True)
    date_created =  Column(DateTime)
    date_modified = Column(DateTime)
    agent = Column(String)
    target = Column(String)

    def __repr__(self):
        return "<Noid(identifier='%s', created='%s', modified='%s' user='%s', " \
               "target='%s')>" % (self.identifier, self.date_created, self.date_modified,
                                  self.user, self.target)

    def noid_unique(self):
        """Return TRUE if NOID is unique"""
        return True

    def mint_noid(self):
        noid = ''.join(SystemRandom().choice(ascii_lowercase + digits) for _ in range(10))
        if noid_unique(noid):
            return noid
        else:
            mint_noid(self)


class Org(Base):
    __tablename__ = 'Org'
    org_id = Column(Integer, primary_key=True)
    org_name = Column(String, unique=True)
    admin = Column(Integer)

    def __repr__(self):
        return "<Org(org_name='%s', org_id='%s', admin='%s')>" % (self.org_name, self.org_id,
                                                                  self.admin)


@app.route('/', methods=['GET'])
def show_welcome():
    """Display useful information about the app"""
    return "Hello world!"


@app.route('/noid/api/v1.0/user', methods=['GET'])
def get_users():
    """Retrieve information about users"""
    return "get users"


@app.route('/noid/api/v1.0/user/<username>', methods=['GET'])
def get_profile(username):
    """Retrieve information about a specific user"""
    profile = User.get_user_profile(username)
    print(profile)
    return profile


@app.route('/noid/api/v1.0/identifier/', methods=['GET'])
def get_identifiers():
    """Return list of identifiers"""
    return jsonify({'identifiers': identifiers})


@app.route('/noid/api/v1.0/identifier/<int:identifier>', methods=['GET'])
def get_identifier_metadata(identifier):
    """Return metadata from single identifier"""
    return jsonify(identifiers[identifier])


@app.route('/noid/api/v1.0/identifier/', methods=['POST'])
def mint_identifier():
    """Mint and return identifier"""
    username = request.json['username']
    agent = request.json['agent']
    org = request.json['org']
    title = request.json['title']
    noid = "noid"

    pid = (username, agent, org, title, noid)
    db.session.add(pid)
    db.session.commit()

    return jsonify(pid)


if __name__ == '__main__':
    app.run(debug=True)
