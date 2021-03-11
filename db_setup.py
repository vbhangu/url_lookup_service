import sqlite3


def create_table():
    conn = sqlite3.connect("malware_url.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS malware (url TEXT)")
    conn.commit()
    conn.close()


def insert(url):
    conn = sqlite3.connect("malware_url.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO malware VALUES(?)", (url,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("malware_url.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM malware")
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()

with open("malware_list.txt") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        insert(line.strip())

# print(view())



