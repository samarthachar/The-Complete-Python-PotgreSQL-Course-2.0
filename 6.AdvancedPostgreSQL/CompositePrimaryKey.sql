CREATE TABLE accounts (
    account_number INTEGER,
    sort_code INTEGER, 
    user_name TEXT,
    PRIMARY KEY(account_number, sort_code)
);

CREATE TABLE customer_details (
    id SERIAL PRIMARY KEY,
    full_name TEXT,
    address TEXT,
    mobile TEXT,
    account_number INTEGER,
    sort_code INTEGER,
    FOREIGN KEY (account_number, sort_code) REFERENCES accounts /*(account_number, sort_code)*/