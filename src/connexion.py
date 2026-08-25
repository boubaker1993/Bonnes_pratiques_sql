import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import (
    Engine,  # <-- Import depuis sqlalchemy.engine pour le typage
)

load_dotenv()


def get_engine() -> Engine:
    """Crée et retourne l'engine SQLAlchemy."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL manquante dans le .env")
    return create_engine(url)


engine = get_engine()
