import os
from datetime import timedelta

class Config:
    SECRET_KEY = '123'
    POSTGRES_USERNAME = "postgres"
    POSTGRES_PASSWORD = "pass1234"
    POSTGRES_DB_NAME = "FLask_db"
    POSTGRES_PORT = 5432
    POSTGRES_HOST = 'localhost'
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ditambah
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_SECRET_KEY = "super-secret"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
