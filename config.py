import os
class Configuration(object):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:''@localhost/corporate'
    #SQLALCHEMY_DATABASE_URI=os.environ('CLEARDB_DATABASE_URL')
    #mysql://b49680054be872:18a9dcb2@us-cdbr-iron-east-05.cleardb.net/heroku_a28949ef640e9b2?reconnect=true
    #SQLALCHEMY_DATABASE_URI='mysql://b49680054be872:18a9dcb2@us-cdbr-iron-east-05.cleardb.net/heroku_a28949ef640e9b2?reconnect=true/corporate'
    #CLEARDB_DATABASE_URL = 'mysql://b49680054be872:18a9dcb2@us-cdbr-iron-east-05.cleardb.net/heroku_a28949ef640e9b2?reconnect=true'

    #MYSQL_HOST = 'us-cdbr-iron-east-05.cleardb.net'
    #MYSQL_USER = 'b49680054be872'
    #MYSQL_PASSWORD = '18a9dcb2'
    #MYSQL_DB = 'heroku_a28949ef640e9b2'