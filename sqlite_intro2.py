import sqlite3
import numpy as np

conn = sqlite3.connect('vector-db.db')

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vectors (
        id INTEGER PRIMARY KEY,
        vector BLOB NOT NULL
    )
    """
)

vect1 = np.array([1.2,3.4,2.1,0.8])
vect2 = np.array([2.7,1.5,3.9,2.3])

cursor.execute(
    " INSERT INTO vectors (vector) VALUES (?)",
    (sqlite3.Binary(vect1.tobytes()),)
)

cursor.execute(
    " INSERT INTO vectors (vector) VALUES (?)",
    (sqlite3.Binary(vect2.tobytes()),)
)

# cursor.execute(
#     "SELECT vector FROM vectors"
# )

# rows = cursor.fetchall()
# print(rows)

# vector1 = np.frombuffer(rows[0][0], dtype=np.float64)
# vector2 = np.frombuffer(rows[1][0], dtype=np.float64)
# print(vector1)

# for row in rows:
#     v = np.frombuffer(row[0], dtype=np.float64)
#     print(v)

query_vector = np.array([1.0,3.2,2.0,0.5])
cursor.execute(
    "SELECT vector FROM vectors ORDER BY (vector - ?) ASC",
    (sqlite3.Binary(query_vector.tobytes()),)
)

res = cursor.fetchone()
v = np.frombuffer(res[0], dtype=np.float64)
print(v)