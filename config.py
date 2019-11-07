class Configuration(object):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True
   # CLEARDB_DATABASE_URL='mysql+mysqlconnector://root:''@localhost/corporate'
    CLEARDB_DATABASE_URL = 'mysql://b49680054be872:18a9dcb2@us-cdbr-iron-east-05.cleardb.net/heroku_a28949ef640e9b2?reconnect=true'