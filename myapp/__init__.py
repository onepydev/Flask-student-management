import sentry_sdk
from flask import Flask, request
from flask_sqlalchemy  import SQLAlchemy
#from flask_script import Manager
from flask_migrate import Migrate
from flask_mail import Mail
import os
from sentry_sdk.integrations.flask import FlaskIntegration
import logging


app = Flask(__name__, instance_relative_config=True,template_folder='templates')
app.config.from_pyfile('config.py')
appconfig=app.config
mail=Mail(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refersjj to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
logging.basicConfig(
        level=logging.DEBUG,
        filename="applogs.log"
        ) 


#sentry_sdk.init(
    #dsn=appconfig['SENTRY_LOG_API'],
    #integrations=[FlaskIntegration()],
    #traces_sample_rate=1.0,
#)

db=SQLAlchemy(app)
migrate = Migrate(app,db)

from .api.apihandler import  apiview
app.register_blueprint(apiview,url_prefix='/api')


@app.after_request
def after_request(response):    
    return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


### Flask Migrate ### Flask
# ensure virtial environment is on the
# pip install Flask-migrate
