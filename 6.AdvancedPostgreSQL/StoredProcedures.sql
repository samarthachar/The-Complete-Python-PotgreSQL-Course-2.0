CREATE PROCEDURE insert_test_data() AS $$
BEGIN
    DROP TABLE IF EXISTS test_data;
    CREATE TABLE test_data (id INTEGER, name TEXT);
    INSERT INTO test_data VALUES (1, 'Bob');
    INSERT INTO test_data VALUES (2, 'Rolf');
    COMMIT;
END;
$$ LANGUAGE plpgsql;

CALL insert_test_data();