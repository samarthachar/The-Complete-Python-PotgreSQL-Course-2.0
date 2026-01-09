CREATE TABLE users (name TEXT, email TEXT, last_opened INTEGER);

INSERT INTO users VALUES ('Bob Smith', 'bobsmith@example.com', 65615);
INSERT INTO users VALUES ('Rolf Smith', 'rolfsmith@example.com', 8587597);
INSERT INTO users VALUES ('Susan Williams', 'susanwilliams@example.com', 56);
INSERT INTO users VALUES ('Anne Pun', 'annepun@example.com', 2419200);

CREATE OR REPLACE FUNCTION delete_inactive(seconds NUMERIC) RETURNS BIGINT AS $$
    with deleted as (DELETE FROM users WHERE last_opened > seconds RETURNING *)
    SELECT COUNT(*) FROM deleted;
$$ LANGUAGE SQL;

SELECT delete_inactive(806400);

DROP FUNCTION delete_inactive(NUMERIC)

SELECT * FROM users;