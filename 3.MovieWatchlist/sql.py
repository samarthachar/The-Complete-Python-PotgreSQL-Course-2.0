CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """ CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (%s, %s);"
INSERT_USER = "INSERT INTO users (username) VALUES (%s)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s;"
SELECT_WATCHED_MOVIES = """SELECT id, title, release_timestamp 
FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN users on users.username = watched.user_username
WHERE username = %s;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (%s , %s);"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 where title = %s;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE %s;"