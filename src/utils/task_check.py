import asyncio
from html import escape 

from datetime import datetime
from aiogram import Bot, Dispatcher
from db.get_cases import get_tasks_by_time  # Импорт функции для получения задач
from aiogram.types import Message

from bot_instance import bot  # Импорт объекта bot

async def periodic_task_check():
    """
    Функция для периодической проверки задач в базе данных и отправки уведомлений в чат.
    """
    while True:
        current_time = datetime.now().replace(second=0, microsecond=0)  # Округляем до минут
        tasks = get_tasks_by_time(current_time)

        if tasks:
            for task in tasks:
                chat_id = task.dealId.companyId.userId.settings.get().telegramChatId
                are_notifications_allowed = task.dealId.companyId.userId.settings.get().telegramSendMessage
                if is_valid_chat_id_and_notifications(chat_id, are_notifications_allowed):
                    print(chat_id, are_notifications_allowed)
                    message = (
                            f"User: {escape(str(task.dealId.companyId.userId.name))}\n"
                            f"Company: {escape(str(task.dealId.companyId.name))}\n"
                            f"Deal: {escape(str(task.dealId.name))}\n"
                            f"Created At: {escape(str(task.createdAt))}\n"
                            f"Type: {escape(task.type)}\n"
                            f"Comment: {escape(task.comment) if task.comment else 'No comment'}\n"
                            f"Date: {escape(str(task.date)) if task.date else 'No date'}\n"
                            f"Finished: {'Yes' if task.finished else 'No'}\n"
                        )
                    await bot.send_message(chat_id=chat_id, text=message)
                else:print("Ошибка: chat_id должен быть числом, и уведомления должны быть разрешены")
        else:
            print(f"No tasks found at {current_time}.")

        await asyncio.sleep(60)  # Ожидание одной минуты перед следующей проверкой


def is_valid_chat_id_and_notifications(chat_id, are_notifications_allowed):
    try:
        # Попытка преобразования chat_id в int и проверка are_notifications_allowed
        return int(chat_id) and are_notifications_allowed is True
    except (ValueError, TypeError):
        return False  # Возвращает False, если преобразование не удалось или есть ошибка