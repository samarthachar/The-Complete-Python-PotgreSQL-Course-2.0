CREATE_POLLS = "CREATE TABLE IF NOT EXISTS polls (id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"
CREATE_OPTIONS = "CREATE TABLE IF NOT EXISTS options (id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER);"
CREATE_VOTES = "CREATE TABLE IF NOT EXISTS votes (username TEXT, option_id INTEGER, vote_timestamp INTEGER);"


SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL = "SELECT * FROM polls WHERE id = %s;"
SELECT_LATEST_POLL = """SELECT * FROM polls
WHERE polls.id = (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
);"""

SELECT_POLL_OPTIONS = "SELECT * FROM options WHERE poll_id = %s;"
SELECT_OPTION = "SELECT * FROM options WHERE id = %s;"

SELECT_VOTES_FOR_OPTION = "SELECT * FROM votes WHERE option_id = %s;"

INSERT_POLL_RETURN_ID = "INSERT INTO polls (title, owner_username) VALUES (%s, %s) RETURNING id;"
INSERT_OPTION = "INSERT INTO options (option_text, poll_id) VALUES (%s, %s) RETURNING id;"
INSERT_VOTE = "INSERT INTO votes (username, option_id, vote_timestamp) VALUES (%s, %s, %s);"
