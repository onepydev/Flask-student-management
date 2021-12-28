from myapp import app,db

if __name__ =="__main__":
    #db.create_all()
    app.run(debug=True,port=5112,host= '127.0.0.1',threaded=True)
    #manager.run()
    ## na to manage am  henry
#$ python manage.py db init 
#$ python manage.py db migrate
#$ python manage.py db upgrade
#$ python manage.py db --help
# To migrate the Db, first disable the app.run then enable the manager.run then run the python commands on poweer shell


