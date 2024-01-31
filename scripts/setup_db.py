import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("CREATE TABLE path(id, label, path)")

cur.execute("INSERT INTO path VALUES ('id1', 'testpath', '/home/jakob')")