import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="composetest-db-1",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
