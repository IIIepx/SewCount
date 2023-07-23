import os
import sys
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%d-%m %H:%M",
    filename="sbot.log",
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(name)-10s: %(levelname)-8s %(message)s")
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)


root_id = int(os.environ["ROOT_USER"])
bot = Bot(token=os.environ["BOT_API"])
dp = Dispatcher(storage=MemoryStorage())


async def main():
    logging.info("Запуск бота")
    await dp.start_polling(bot, dp=dp, root_id=root_id)


if __name__ == "__main__":
    asyncio.run(main())
