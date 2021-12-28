from flask import request,jsonify
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from  myapp import db
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from marshmallow.utils import EXCLUDE
from myapp.api.apimodels import AdminRegisterValidate, AdminloginWithEmail
from myapp.appclass.admin_class import AdminClass
from myapp.models import TokenBlocklist

def is_token_revoked(jti):
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).first()
    if token:
        return True
    else:
        return False

class AdiminRegistration(Resource):
    def post(self):
        json_data=request.get_json()

        if not json_data:
            return {"status":2,"message":'Invalid request'},400
        try:
            AdminRegisterValidate().load(json_data,unknown=EXCLUDE)
        except ValidationError as err:
            return err,400
        
        Admin=AdminClass()
        response=Admin.AdminRegister(fname=json_data['fname'],
                                     sname=json_data['sname'],
                                     email=json_data['email'],
                                     password=json_data['password'],
                                     username=json_data['username'])
        return response,response['code']
    
class  AdiminLogin(Resource):
    def post(self,**kwargs):
        json_data=request.get_json()

        if not json_data:
            return {"status":2,"message":'Invalid request'},400
        try:
            AdminloginWithEmail().load(json_data,unknown=EXCLUDE)
        except ValidationError as err:
            return err,400
        
        Admin=AdminClass()
        response=Admin.AdminLogin(json_data['username'],json_data['password'])
        return response,response['code']

class  AdminLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        Admin=AdminClass()
        response=Admin.Adminlogout(jti)
        return response,response['code']
