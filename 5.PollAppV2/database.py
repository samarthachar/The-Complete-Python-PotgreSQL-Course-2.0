from sql import *
from psycopg2.extras import execute_values

Poll = tuple[int, str, str]
Option = tuple[int, str, int]
Vote = tuple[str, int]

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


# -- Polls --

def create_poll(connection, title: str, owner: str, options: list[str]):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_POLL_RETURN_ID,(title,owner))

            poll_id = cursor.fetchone()[0]
            return poll_id

def get_polls(connection) -> list[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()

def get_poll(connection, poll_id: int) -> Poll:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL, (poll_id,))
            return cursor.fetchone()


def get_latest_poll(connection) -> Poll:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchone()


def get_poll_options(connection, poll_id: int)  -> list[Option]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
            return cursor.fetchall()
        
# -- options --

def get_option(connection, option_id: int) -> Option:
    with connection:
        with connection.cursor() as cursor:
            cursor.excecute(INSERT_POLL_RETURN_ID, (option_id,))
            option_id = cursor.fetchone()[0]
            return option_id
def add_option(connection, option_text, poll_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.excecute(INSERT_OPTION, (option_text, poll_id))

# -- votes --
def get_votes_for_option(connection, option_id: int) -> list[Vote]:
    return


            

def add_poll_vote(connection, username: str, option_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))

            