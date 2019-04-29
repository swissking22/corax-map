import os

DEBUG = True
SECRET_KEY = '3NI6M4'


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir + 'coraxdb.sqlite')
SQL_TRACK_MODIFICATIONS = False