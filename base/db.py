import sqlite3
import logging

con = sqlite3.connect("base/booker.db")
cur = con.cursor()

logger = logging.getLogger(__name__)


def init_db():
    with open("createdb.sql", "r") as file:
        cur.executesqript(file.read())
        con.commit()
    logger.debug("Creating data base")


def check_db_exists():
    cur.execute("select name from sqlite_master where type='table' and name='users'")
    table_exists = cur.fetchall()
    if table_exists:
        return
    init_db()
