import sqlite3


def execute_db(db: str, command: str) -> int:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(command)
    con.commit()
    row_count = cur.rowcount
    return row_count


def get_cursor(db: str):
    con = sqlite3.connect(db)
    cur = con.cursor()
    return cur


def get_res(db: str, command: str) -> list[any]:
    con = sqlite3.connect(db)
    cur = con.cursor()
    res = con.execute(command)
    return list(res.fetchall())
