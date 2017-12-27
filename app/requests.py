from .models import Movie

#Getting the secret key
secret_key = None

def configure_request(app):
    global secret_key
    secret_key = app.config['SECRET_KEY']
    