from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self,**kwargs):
        return {"message":"This is a hello world application"}
    def post(self):
        json_data=request.get_json()
        if not json_data:
            return {"message":'Invalid request'},400
        else:
            return {"message":"Your request for saved"}
        


api.add_resource(HelloWorld,"/")


if __name__ =="__main__":
    app.run(debug=True,port=5112,host= '127.0.0.1')


