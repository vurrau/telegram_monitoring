from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
API_TELEGRAM = os.environ.get('API_TELEGRAM')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"