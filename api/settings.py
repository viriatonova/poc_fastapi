import os

# Variáveis de ambiente

DEBUG = os.getenv("DEBUG")
RELOAD = os.getenv("RELOAD") 

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

API_HOST = os.getenv("API_HOST") 
PORT = int(os.getenv("API_PORT"))
DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
