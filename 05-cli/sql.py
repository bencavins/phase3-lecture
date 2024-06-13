create_table = """
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)
"""


insert_score = """
INSERT INTO scores (name, score)
VALUES
(?, ?)
"""