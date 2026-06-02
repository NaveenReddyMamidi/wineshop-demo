import os
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(Path(basedir) / ".env")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_wine_shop_secret_key")
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+pg8000://", 1)

    SQLALCHEMY_DATABASE_URI = database_url or "postgresql://appuser:K4T3HkbtFgxGTYPLxTdwUta9k92UbMDX@dpg-d8f3jfl53gjs739l6ptg-a/wineshop_db?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
