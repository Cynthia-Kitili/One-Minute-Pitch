import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'TheDifference'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vincent:Empharse333@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}