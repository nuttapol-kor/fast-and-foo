import os
from dotenv import load_dotenv
load_dotenv()
OPENAPI_AUTOGEN_DIR = os.environ.get("OPENAPI_AUTOGEN_DIR")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWD = os.environ.get("DB_PASSWD")
DB_NAME = os.environ.get("DB_NAME")
