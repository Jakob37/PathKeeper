#!/usr/bin/env python3

import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("CREATE TABLE path(id, label, path, alias)")

cur.execute("INSERT INTO path VALUES ('id1', 'testpath', '/home/jakob', 'testalias')")

# Show all tables
# https://docs.python.org/3/library/sqlite3.html
# res = cur.execute("SELECT name FROM sqlite_master")

# New column
# cur.execute("ALTER TABLE path ADD alias")

# .tables
# .schema path
