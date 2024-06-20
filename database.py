import pymysql
import os

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db=os.getenv('db'),
  password=os.getenv("PASSWORD"),
  host=os.getenv('host'),
  user=os.getenv('user'),
  read_timeout=timeout,
  port=25039,
  write_timeout=timeout,
)

def get_data():
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM events")
        result = cursor.fetchall()
    finally:
        connection.close()
    return result