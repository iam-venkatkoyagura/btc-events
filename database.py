import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-3bbc87ea-venkat-e0d8.j.aivencloud.com",
  password="AVNS_Zt0Hik6JPblq25Ndbsq",
  read_timeout=timeout,
  port=25039,
  user="avnadmin",
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