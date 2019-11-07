import os,sys
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_mail import Mail
import gunicorn
import mysql
#import WSGIserver
app = Flask(__name__)
app.config.from_object(Configuration)
db = mysql(app)


migrate = Migrate(app, db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)




app.config['DEBUG']=True
app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_DEBUG']=True
app.config['MAIL_USERNAME']='gevman97@gmail.com'
app.config['MAIL_PASSWORD']='cnvytaqaywxtfdve'
app.config['MAIL_DEFAULT_SENDER'] = 'admin@gmail.com'
app.config['MAIL_MAX_EMAILS']=None
app.config['MAIL_SUPPRESS_SEND']=False
app.config['MAIL_ASCII_ATTACHMENTS']=False
mail=Mail(app)

#sys.path.insert(0, "/home/flasktest/www/flasktest.atservers.net")
#os.chdir("/home/flasktest/www/flasktest.atservers.net")
#if __name__ == '__main__':
#    WSGIServer(app).run()