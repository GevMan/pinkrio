class Configuration(object):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO = True
    CLEARDB_BROWN_URL='mysql+mysqlconnector://root:''@localhost/corporate'