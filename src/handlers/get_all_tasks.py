from aiogram.types import Message
from aiogram.filters import Command

from utils.task_utils import send_tasks_to_telegram

from db.db_init import initialize_db, close_db
from db.get_cases import get_all_tasks

from bot_instance import dp
@dp.message(Command("tasks"))
async def report_tasks_handler(message: Message) -> None:

    initialize_db()
    # Получение задач из базы данных
    tasks = get_all_tasks()
    await send_tasks_to_telegram(tasks, chat_id=message.chat.id)

    # Закрытие подключения к базе данных
    close_db()