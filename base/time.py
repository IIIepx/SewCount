import logging
import sqlite3
from pytimeparse import parse
from typing import Dict, Tuple, List
from datetime import datetime, timedelta
from base import db

cur = db.cur
con = db.con

logger = logging.getLogger("__name__")


def save_time(user: int, time: timedelta) -> float:
    seconds = parse(str(time))
    logger.info(f"{seconds} ============ type {type(seconds)}")
    cur.execute(f"select stage from actual where user={user}")
    stage_id = cur.fetchone()[0]
    cur.execute(f"select id, hours from timerecords where stage={stage_id}")
    try:
        id, hours = cur.fetchone()
    except:
        cur.execute(
            "insert into timerecords (hours, user, stage) values (?, ?, ?)",
            (seconds, user, stage_id),
        )
        con.commit()
        return seconds
    logger.info(f"{id} , {hours}")
    seconds += hours
    cur.execute(f"update timerecords set hours='{seconds}' where id={id}")
    con.commit()
    return seconds
