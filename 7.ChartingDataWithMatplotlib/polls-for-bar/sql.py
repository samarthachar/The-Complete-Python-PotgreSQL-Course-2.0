SELECT_POLLS_AND_VOTES = """
SELECT polls.title, SUM(votes.option_id) FROM polls
JOIN options ON options.poll_id = polls.id
JOIN votes on options.id = votes.option_id
GROUP BY polls.title;
"""