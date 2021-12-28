from flask import Flask
from flask import Blueprint,jsonify
from myapp import app
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from myapp.api.resources.student_management import (
    AddStudent,
    FetchStudent,
    FetchOneStudent,
    FetchStudentPagination,
    ManageStudent
)

from myapp.api.resources.admin_management import AdiminLogin,AdiminRegistration,is_token_revoked,AdminLogout

    
app.config['JWT_BLACKLIST_ENABLED'] = True  # enable blacklist feature

apiview = Blueprint("apiview", __name__)
api = Api(apiview,errors=Flask.errorhandler)
jwt = JWTManager(app)
CORS(app)

# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return is_token_revoked(jti)  


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return jsonify({
        "status":2,
        "message":  'Access token expired',

    }), 401


    
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "status":2,
        "message": "Request does not contain an authorization token.",
    }), 401

#This decorator sets the callback function for returning a custom response when an invalid JWT is encountered.
@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        "status":2,
        "message":  'Signature verification failed.',
    }), 401


#This decorator sets the callback function for returning a custom response when a revoked token is encountered.
@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "status":2,
        "message":  "Access token has been revoked",
    }), 401


api.add_resource(AddStudent,'/addstudent/')
api.add_resource(FetchStudent,'/fetchstudents/')
api.add_resource(FetchStudentPagination,'/fetchstudentsapagination/<int:page>')
api.add_resource(FetchOneStudent,'/fetchstudents/<string:username>')
api.add_resource(ManageStudent,'/managestudent/<string:username>')

## Admin  Section ##
api.add_resource(AdiminRegistration,'/adminregister/')
api.add_resource(AdiminLogin,'/adminlogin/')
api.add_resource(AdminLogout,'/adminlogout/')





