from marshmallow import fields,validate
from flask_marshmallow import Marshmallow  
import json
import re

from datetime import date    


def check_email(email):  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        return True 
          
    else:  
       return False

ma = Marshmallow()
not_blank = validate.Length(min=1, error='Field cannot be blank')

class loginWithEmail(ma.Schema):
    userid=fields.String(required=True,validate=not_blank)  ## will be Email or Phone number
    password=fields.String(required=True,validate=not_blank)
    appversion=fields.String(required=True,validate=not_blank)
    
class AddStudentValidator(ma.Schema):
    fname=fields.String(required=True,validate=not_blank)
    sname=fields.String(required=True,validate=not_blank) 
    email=fields.Email(required=True,validate=not_blank) 
    username=fields.String(required=True,validate=not_blank) 
    studentclass=fields.String(required=True,validate=not_blank) 

class AdminloginWithEmail(ma.Schema):
    username=fields.String(required=True,validate=not_blank)  ## will be Email or Phone number
    password=fields.String(required=True,validate=not_blank)

class AdminRegisterValidate(ma.Schema):
    username=fields.String(required=True,validate=not_blank)  ## will be Email or Phone number
    password=fields.String(required=True,validate=not_blank)
    email=fields.Email(required=True,validate=not_blank)
    fname=fields.String(required=True,validate=not_blank)
    sname=fields.String(required=True,validate=not_blank)

