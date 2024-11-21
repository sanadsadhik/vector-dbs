import sqlite3

conn = sqlite3.connect('')

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
    )
    """
)

cursor.execute(
    " INSERT INTO employees (name,age,department) VALUES (?,?,?)",
    ("John Doe", 30, "Sales")
)

cursor.execute(
    "SELECT * FROM employees"
)

rows = cursor.fetchall()
print(rows)