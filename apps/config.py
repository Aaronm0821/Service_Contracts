import os
import yaml
from dotenv import load_dotenv
from enum import Enum

load_dotenv()

ROOT = os.getcwd()
with open(ROOT + "/apps/config.yml") as f:
    CONFIG_FILE = yaml.load(f, Loader=yaml.FullLoader)

CONFIG = CONFIG_FILE["DEV"]


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Assets Management
    ASSETS_ROOT = "/static/assets"

    # Set up the Apps corresponding DB Connects
    SERVER = CONFIG.get("DB_SERVER")
    USER = os.environ.get("DB_USER")
    PASSWORD = os.environ.get("DB_PW")
    DATABASE_NAME = CONFIG.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pymssql://{USER}:{PASSWORD}@{SERVER}/{DATABASE_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ACCESS_LEVELS = {"Normal": 1, "Manager": 2, "Support": 3}


app_config = Config
