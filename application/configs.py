# -*- coding: utf-8 -*-
import os
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config(object):
    SECRET_KEY = '^753*&FdFS#4D'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.sqlite')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
