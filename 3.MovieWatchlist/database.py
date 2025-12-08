import datetime
from sql import *
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp)"


connection = psycopg2.connect(os.environ["DATABASE_URL"])

def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)
            cursor.execute(CREATE_RELEASE_INDEX)

def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()

def search_movies(search_term):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
            return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (username,))
            return cursor.fetchall()
