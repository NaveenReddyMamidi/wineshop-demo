import os
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(Path(basedir) / ".env")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret")
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+pg8000://", 1)

    SQLALCHEMY_DATABASE_URI = database_url or "postgresql+pg8000://postgres:postgres@localhost:5432/wineshop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
