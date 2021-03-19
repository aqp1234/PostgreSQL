import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='',
    pw='',
    url='localhost',
    db='testdata')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'dev'
