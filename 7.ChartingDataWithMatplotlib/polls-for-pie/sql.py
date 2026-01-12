SELECT_POLLS = "SELECT * FROM polls;"
SELECT_OPTIONS_IN_POLL = """
SELECT options.option_text, SUM(votes.option_id) FROM options
JOIN polls ON options.poll_id = polls.id
JOIN votes on options.id = votes.option_id
WHERE polls.id = %s
GROUP BY options.option_text;
"""