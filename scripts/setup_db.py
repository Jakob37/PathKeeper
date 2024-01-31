import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("CREATE TABLE path(id, label, path)")

cur.execute("INSERT INTO path VALUES ('id1', 'testpath', '/home/jakob')")

# https://docs.python.org/3/library/sqlite3.html
res = cur.execute("SELECT name FROM sqlite_master")
