import sqlite3


def execute_db(db: str, command: str):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(command)
    con.commit()


def get_cursor(db: str):
    con = sqlite3.connect(db)
    cur = con.cursor()
    return cur
