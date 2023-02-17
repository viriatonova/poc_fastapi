import os

# from os.path import join

# from dotenv import load_dotenv

# root_dir = os.path.dirname(os.path.abspath('.env'))
# dotenv_path = join(root_dir, '.env')
# load_dotenv(dotenv_path)


# Variáveis de ambiente
DEBUG = os.getenv("DEBUG")
RELOAD = os.getenv("RELOAD") 
API_HOST = os.getenv("API_HOST") 
PORT = int(os.getenv("API_PORT"))
DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
