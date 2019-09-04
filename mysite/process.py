import sqlite3
from sqlite3 import Error
def connect_db():
    conn = None
    try:
        conn = sqlite3.connect('maindb.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
        return 0

    return conn

def check_login(email,entered_password):
    conn= connect_db()
    if conn !=0:
        cur=conn.cursor()
        row_count=cur.execute("select * from user where email = ? ", (email,))
        data = cur.fetchall()
        password=''
        print(row_count, data)
        if conn:
            conn.close()
        for row in data:
            a,b,c,password=row
            print(password)
            if entered_password==password :
                return True
        return False

#print(check_login('m@m()','mb1'))
