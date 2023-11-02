import os
from datetime import timedelta

class Config:
    SECRET_KEY = '123'
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "pass1234"
    MYSQL_DB_NAME = "Flask_sql"
    MYSQL_PORT = 3306
    MYSQL_HOST = 'localhost'
    
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ditambah
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_SECRET_KEY = "super-secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
