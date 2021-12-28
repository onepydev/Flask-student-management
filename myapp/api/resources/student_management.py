from flask import request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from marshmallow.utils import EXCLUDE
from myapp.api.apimodels import  AddStudentValidator
from myapp.appclass.student_class import StudentClass
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

class  AddStudent(Resource):
    @jwt_required()
    def post(self):
        json_data=request.get_json()
        if not json_data:
            return {"status":2,"message":"Invalid request"},400
        
        try:
             AddStudentValidator().load(json_data,unknown=EXCLUDE)
        except ValidationError as err:
            return err,400
        
        newStudent=StudentClass()
        response=newStudent.AddStudent(json_data)
        return response,response['code']
        
        
    
class  FetchStudent(Resource):
    @jwt_required()
    def get(self):
        GetStudents=StudentClass()
        response=GetStudents.FetchAllStudents()
        return response,response['code']

class FetchStudentPagination(Resource):
    @jwt_required()
    def get(self,**kwargs):
        page=kwargs.get('page')
        perPage=1
        GetStudents=StudentClass()
        response=GetStudents.FetchAllStudentsPagination(page,perPage)
        return response,response['code'] 
        
class  FetchOneStudent(Resource):
    @jwt_required()
    def get(self,**kwargs):
        """ Get one student"""
        GetStudents=StudentClass()
        username=kwargs.get('username')
        response=GetStudents.GetOneStudents(username)
        return response,response['code']   
    
class  ManageStudent(Resource):
    @jwt_required()
    def put(self,**kwargs):
        json_data=request.get_json()
        if not json_data:
            return {"status":2,"message":'Invalid request'},400
        
        Update=StudentClass()
        username=kwargs.get('username')
        response=Update.UpdateStudent(json_data,username)
        return response,response['code']
    
    @jwt_required()
    def delete(self,**kwargs):
        Delete=StudentClass()
        username=kwargs.get('username')
        response=Delete.DeleteStudent(username)
        return response,response['code']
          
    

