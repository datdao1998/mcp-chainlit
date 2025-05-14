import psycopg2
from setup.config import config

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**config.db_config)
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        raise