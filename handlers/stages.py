from aiogram import Router, F, types

from collections.abc import Callable, Iterable
import os
import sys
import asyncio
import logging
from typing import Callable, Dict, Any, Awaitable
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, Update
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from base import db, users, service

rt = Router()

@rt.message(F.text.startwith == "проект")
async def  cmd_projects(msg: types.Message):

