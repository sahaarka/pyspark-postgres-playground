import os
import psycopg2
from psycopg2.extras import execute_values

DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_NAME = os.getenv("POSTGRES_DB", "leetcode")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgrespw")

conn = psycopg2.connect(
    host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
    user=DB_USER, password=DB_PASS
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT,
    hire_date DATE
);
""")

rows = [
    ('Alice','HR',70000,'2019-03-15'),
    ('Bob','Engineering',90000,'2018-08-01'),
    ('Carol','Sales',60000,'2020-01-10'),
    ('Dave','Engineering',110000,'2017-11-21'),
]
execute_values(cur,
               "INSERT INTO employees (name, department, salary, hire_date) VALUES %s ON CONFLICT DO NOTHING",
               rows)
conn.commit()
cur.close()
conn.close()
print("Seed complete")