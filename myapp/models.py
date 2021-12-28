from myapp import db
from sqlalchemy import  DateTime,func
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql import func


class Students(db.Model):
    __tablename__ = 'students'
   
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    sname = db.Column(db.String(50), nullable=False)
    username=db.Column(db.String(50), nullable=False,unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    student_class = db.Column(db.String(50), nullable=False)
    last_updated=db.Column(DateTime(timezone=True), onupdate=func.now(),nullable=True)
    rdate =db.Column(db.DateTime, nullable=False,  default=func.now())


class Admins(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    sname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
    username=db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(150), nullable=False)
    rdate =db.Column(db.DateTime, nullable=False,  default=func.now())

class TokenBlocklist(db.Model):
    __tablename__="token_blocklist"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    








