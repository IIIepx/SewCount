import logging
from typing import List, Tuple, Dict
from itertools import chain
from base import db

cur = db.cur
con = db.con

logger = logging.getLogger(__name__)

def set_actual(user: int, project: str, stage: str):
    cur.execute(f"select id from projects where user={user} and name='{project}'")
    project_id = cur.fetchone()[0]
    cur.execute(f"select id from stages where project={project_id}")
    stage_id = cur.fetchone()[0]
    cur.execute(f"select id from actual where user={user}")
    logger.info(f"project_id = {project_id}       stage_id = {stage_id}")
    if cur.fetchone()[0]:
        cur.execute(
            f"update actual set stage={stage_id}, project={project_id} where user=={user}"
        )
    else:
        cur.execute(
            f"insert into actual (user, project, stage) values (?, ?, ?)",
            (user, project_id, stage_id),
        )
    con.commit()
