class Configuration(object):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True
    CLEARDB_DATABASE_URL='mysql+mysqlconnector://root:''@localhost/corporate'