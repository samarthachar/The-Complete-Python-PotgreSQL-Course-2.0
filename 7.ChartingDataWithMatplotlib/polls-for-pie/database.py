import os
import psycopg2
from dotenv import load_dotenv 
from sql import *

load_dotenv()



connection = psycopg2.connect(os.environ.get("DATABASE_URI"))

def get_polls():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLLS)
            return cursor.fetchall()

def get_options(poll_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_OPTIONS_IN_POLL, (poll_id,))
            return cursor.fetchall()
        