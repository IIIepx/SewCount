from typing import List, Tuple, Dict
from base import db


cur = db.cur
con = db.con


def get_project(id: int) -> List[Tuple]:
    cur.execute(f"select name from projects where user=={id}")
    return cur.fetchone()
