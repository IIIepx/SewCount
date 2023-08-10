from base import db

cur = db.cur
con = db.con


def delete_tables():
    """Удаляет и создает заново все таблицы, кроме user"""

    for name in ("projects", "stages", "timerecords"):
        cur.execute(f"drop table {name}")
    con.commit()

    db.init_db()


def add_user(id: int, name: str):
    cur.executemany("insert into users (id, name) values (?, ?)", [(id, name)])
    con.commit()
