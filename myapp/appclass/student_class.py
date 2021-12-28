
from flask import jsonify
from myapp import db,app
from myapp.models import Students
import logging

class StudentClass():
    
    
    def AddStudent(self,data):
        """ This method will add a new student to our database. """
        """ Check to ensure incoming email data does not exists already"""
        checkEmailAndUsername=db.session.query(Students.username)\
            .filter((Students.email==data['email']) | (Students.username==data['username'])).first()
        
        if checkEmailAndUsername:
            return  {"status":2,"message":"Email or username already registered","code":409}
        try:
            newStudent=Students()
            newStudent.fname=data['fname']
            newStudent.sname=data['sname']
            newStudent.email=data['email']
            newStudent.student_class=data['studentclass']
            newStudent.username=data['username']
            db.session.add(newStudent)
            db.session.commit()
            
        except Exception as e:
            ### logger here ##
            print(e)
            return  {"status":2,"message":"An error occured while adding {} {}  was added to students table".format(data['fname'],data['sname']),"code":500}
            
        else:
            return  {"status":1,"message":"You have successfully {} {}  was added to students table".format(data['fname'],data['sname']),"code":200}
        
    
    def FetchAllStudents(self):
        """ This method will fetch all the students from the database"""
      
        try:
            AllStudents=db.session.query(Students.fname,Students.sname,Students.email,Students.username).all()
            
        except Exception as e:
            ### logger here ##
            print(e)
            return  {"status":2,"message":"An error occured while fetching students","code":500}
            
        else:
            all_students=[]
            if  not AllStudents:
                ## Check if we have data##
                return {"status":2,"message":"No student found","code":404}
            else:
                
                for  i in AllStudents:
                    all_students.append(i._asdict())
                    
                return  {"status":1,"message":"All students successfully retrieved","data":all_students,"code":200}
    
    def GetOneStudents(self,username):
        """ This method will fetch one student from the database using the username and search key"""
        try:
            
            fetchOneStudent=db.session.query(Students.fname,Students.sname,Students.email,Students.username).filter(Students.username==username).first()

        except Exception as e:
            ###  Technical error or dev only ##
            print(e)
            return  {"status":2,"message":"Error occured.Could not fetch student {} ".format(username),"code":500}
            
        else:
            
            if  not fetchOneStudent:
                ## Check if we have data##
                return {"status":2,"message":"No student found","code":404}
            else:
                
                return  {"status":1,"message":"All students successfully retrieved","data":fetchOneStudent._asdict(),"code":200}
    
    
    def FetchAllStudentsPagination(self,page,per_page):
        """ This class will fetch all the students from the database"""
      
        try:
            AllStudents=db.session.query(Students.fname,Students.sname,Students.email,Students.username).order_by(Students.id.desc())\
            .paginate(page=page,per_page=per_page,error_out=False)
            
        except Exception as e:
            ### logger here ##
            print(e)
            return  {"status":2,"message":"An error occured while fetching students","code":500}
            
        else:
            all_students=[]
            if  not AllStudents:
                ## Check if we have data##
                return {"status":2,"message":"No student found","code":404}
            else:
                
                for  i in AllStudents.items:
                    all_students.append(i._asdict())
                    
                return  {"status":1,"message":"All students successfully retrieved","data":all_students,"code":200}
    
    def UpdateStudent(self,data,username):
        checkUser=db.session.query(Students.username)\
            .filter(Students.username==username).first()
        
        if not  checkUser:
            app.logger.warning('Student not found')
            
            return  {"status":2,"message":"User with username not found","code":404}
        
        try:
            Students.query.filter_by(username=username).update(data)
            db.session.commit()
        except Exception as e:
            ### logger here ##
            print(e)
            return  {"status":2,"message":"An error occured while updating student data","code":500}
            
        else:
            return  {"status":1,"message":"Record successfully updated","code":200}
        
    def DeleteStudent(self,username):
        checkUser=db.session.query(Students.username)\
            .filter(Students.username==username).first()
        
        if not  checkUser:
            return  {"status":2,"message":"User with username not found","code":404}
        
        try:
            Students.query.filter_by(username=username).delete()
            db.session.commit()
        except Exception as e:
            ### logger here ##
            print(e)
            return  {"status":2,"message":"An error occured while updating student data","code":500}
            
        else:
            return  {"status":1,"message":"Student Record successfully deleted","code":200}