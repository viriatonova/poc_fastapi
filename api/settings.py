import os
from dotenv import load_dotenv
from os.path import join

# Using without docker
ROOT_DIR = os.getcwd()
ENV_PATH = join(ROOT_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

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
