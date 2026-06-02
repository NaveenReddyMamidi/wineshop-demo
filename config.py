import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")


class Config:
    # Security
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "my_wine_shop_prod_key"
    )

    # Database URL from environment
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Convert old PostgreSQL URLs if needed
    if (
        SQLALCHEMY_DATABASE_URI
        and SQLALCHEMY_DATABASE_URI.startswith("postgresql://")
    ):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgresql://",
            "postgresql+pg8000://",
            1
        )

    # Fallback for local development only
    if not SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = (
            "postgresql+pg8000://postgres:postgres@localhost:5432/wineshop"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLAlchemy engine options
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
        "pool_size": 10,
        "max_overflow": 20,
    }
