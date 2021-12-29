import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# Statement for enabling the development environment
DEBUG = False

SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONNECTION_STRING")
SQLALCHEMY_TRACK_MODIFICATIONS =False
SQLALCHEMY_ENGINE_OPTIONS = {
    
    'pool_size': 10,
    'pool_recycle':300,
    'pool_pre_ping': True
}

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True
SECRET_KEY = os.environ.get('FLASK_SECRET')
##  MAIL SETTINGS ##
MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
MAIL_SERVER=os.environ.get("MAIL_SERVER")
MAIL_PORT=os.environ.get("MAIL_PORT")
MAIL_USE_TLS=True
MAIL_DEFAULT_SENDER =os.environ.get("MAIL_DEFAULT_SENDER")
MAIL_DEBUG =False
MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
MAIL_TEMPLATE=os.environ.get("MAIL_TEMPLATE")

APPENV=os.environ.get("APPENV")

SENTRY_LOG_API=os.environ.get("SENTRY_lOG_API")
FLASK_SECRET=os.environ.get("FLASK_SECRET")





