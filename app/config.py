import os

class Configure:
    SECRET_KEY = os.environ.get('SECRETT_KEY')
    DEBUG = True