import os
import psycopg2
from dotenv import load_dotenv 
from sql import *

load_dotenv()



connection = psycopg2.connect(os.environ.get("DATABASE_URI"))



def get_polls_and_votes():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLLS_AND_VOTES,)
            return cursor.fetchall()
        