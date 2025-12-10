import psycopg2
from configs.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )
