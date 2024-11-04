import asyncio
import logging
import sys

from utils.task_check import periodic_task_check
from handlers import start_handler, get_all_tasks, echo_handler
from bot_instance import bot, dp

async def main() -> None:
    # And the run events dispatching
    asyncio.create_task(periodic_task_check())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())