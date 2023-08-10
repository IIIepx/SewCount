from collections.abc import Callable, Iterable
import os
import sys
import asyncio
import logging
from typing import Callable, Dict, Any, Awaitable
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message, Update
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from base import db, service, users
from middlewares.adminrights import AccessLimitaionMiddleware


rt = Router()
rt.message.middleware(AccessLimitaionMiddleware())
logger = logging.getLogger(__name__)


@rt.message(Command("q"))
async def cmd_quit(msg: types.Message):
    await msg.answer("Shutdown bot. Buy!")
    logger.debug("Command quit")
    exit()


@rt.message(Command("add"))
async def cmd_add_user(msg: types.Message, users: users):
    cmd = msg.text.split()
    if len(cmd) > 2:
        name = cmd[2] + " " + "" if len(cmd) == 3 else cmd[3]
        try:
            service.add_user(int(cmd[1]), name)
            await msg.answer("Successful")
        except ValueError:
            await msg.answer("ValueError")
    users = [item[0] for item in users.get_users_id()]


@rt.message(Command("drop"))
async def cmd_delete_all_records(msg: types.Message):
    service.delete_tables()
    await msg.answer("Tables is clean")
