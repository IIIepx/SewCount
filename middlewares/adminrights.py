import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message

logger = logging.getLogger(__name__)


class AccessLimitaionMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        logger.debug(data)
        for key, value in data.items():
            logger.debug(f"{key}: {type(value)} = {value}\n")
        if data["event_from_user"].id == data["root_id"]:
            return await handler(event, data)
