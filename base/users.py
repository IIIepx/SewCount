from typing import List, Tuple, Dict
from base import db

cur = db.cur
con = db.con


def get_users_id() -> List[Tuple]:
    cur.execute("select id from users")
    return cur.fetchall()


def get_users() -> List[Tuple]:
    cur.execute("select * from users")
    return cur.fetchall()
