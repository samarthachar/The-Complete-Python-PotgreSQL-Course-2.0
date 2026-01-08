from typing import List, Tuple
from sql import *
from psycopg2.extras import execute_values
from contextlib import contextmanager

Poll = Tuple[int, str, str]
Option = Tuple[int, str, int]
Vote = Tuple[str, int]
PollResults = Tuple[int, str, int, float]

@contextmanager
def get_cursor(connection):
    with connection:
        with connection.cursor() as cursor:
            yield cursor

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


# -- polls --


def create_poll(connection, title: str, owner: str) -> int:
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_POLL_RETURN_ID, (title, owner))

            poll_id = cursor.fetchone()[0]
            return poll_id


def get_polls(connection) -> List[Poll]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_poll(connection, poll_id: int) -> Poll:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_POLL, (poll_id,))
            return cursor.fetchone()


def get_latest_poll(connection) -> List[Poll]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchall()


def get_poll_options(connection, poll_id: int) -> List[Option]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_POLL_OPTIONS, (poll_id,))
            return cursor.fetchall()


# -- options --


def get_option(connection, option_id: int) -> Option:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_OPTION, (option_id,))
            return cursor.fetchone()


def add_option(connection, option_text: str, poll_id: int):
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_OPTION, (option_text, poll_id))


# -- votes --


def get_votes_for_option(connection, option_id: int) -> List[Vote]:
    with get_cursor(connection) as cursor:
            cursor.execute(SELECT_VOTES_FOR_OPTION, (option_id,))
            return cursor.fetchall()


def add_poll_vote(connection, username: str, vote_timestamp: float, option_id: int):
    with get_cursor(connection) as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id, vote_timestamp))
