CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
CREATE TABLE emails (id INTEGER PRIMARY KEY, content TEXT);
CREATE TABLE email_opens (
    email_id INTEGER,
    user_id INTEGER,
    opened_time INTEGER,
    PRIMARY KEY(email_id, user_id),
    FOREIGN KEY (email_id) REFERENCES emails(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users VALUES (1, 'Bob Smith', 'bobsmith@example.com');
INSERT INTO users VALUES (2, 'Rolf Smith', 'rolfsmith@example.com');
INSERT INTO users VALUES (3, 'Susan Williams', 'susanwilliams@example.com');
INSERT INTO users VALUES (4, 'Anne Pun', 'annepun@example.com');

INSERT INTO emails VALUES (1, 'This is a test e-mail');
INSERT INTO emails VALUES (2, 'Another test e-mail.');
INSERT INTO emails VALUES (3, 'We should really write longer e-mails!');

INSERT INTO email_opens VALUES (3, 2, 1572393600);
INSERT INTO email_opens VALUES (2, 2, 1572220800);
INSERT INTO email_opens VALUES (1, 3, 1572393600);
INSERT INTO email_opens VALUES (2, 3, 1572480000);
INSERT INTO email_opens VALUES (1, 4, 1572480000);
INSERT INTO email_opens VALUES (1, 1, 1572393600);

CREATE OR REPLACE FUNCTION opened_ago(email_open_row email_opens) RETURNS DOUBLE PRECISION AS $$
    SELECT cast(extract(epoch FROM CURRENT_TIMESTAMP) AS INTEGER) = email_open_row.opened_time AS  email_opened_ago;
$$ LANGUAGE SQL

SELECT *, opened_ago(email_opens) FROM users
JOIN email_opens ON users.id = email_opens.user_id
WHERE opened_ago(email_opens) < 17509903

SELECT * FROM email_opens JOIN users ON email_opens.user_id = user_id;

SELECT * FROM users; 
