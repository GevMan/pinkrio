import os,sys
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_mail import Mail
import gunicorn
from flaskext.mysql import MySQL
#import WSGIserver
app = Flask(__name__)
app.config.from_object(Configuration)

app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b49680054be872'
app.config['MYSQL_PASSWORD'] = '18a9dcb2'
app.config['MYSQL_DB'] = 'heroku_a28949ef640e9b2'
db = MySQL(app)

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