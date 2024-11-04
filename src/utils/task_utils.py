from html import escape 

from bot_instance import bot
async def send_tasks_to_telegram(tasks, chat_id):
    # Перебираем все задачи и отправляем их по одной
    for task in tasks:
        # Формируем сообщение
        message = (
            f"ChatId: {escape(str(task.dealId.companyId.userId.settings.get().telegramChatId))}\n"
            f"User: {escape(str(task.dealId.companyId.userId.name))}\n"
            f"Company: {escape(str(task.dealId.companyId.name))}\n"
            f"Deal: {escape(str(task.dealId.name))}\n"
            f"Task ID: {escape(str(task.id))}\n"
            f"Created At: {escape(str(task.createdAt))}\n"
            f"Type: {escape(task.type)}\n"
            f"Comment: {escape(task.comment) if task.comment else 'No comment'}\n"
            f"Date: {escape(str(task.date)) if task.date else 'No date'}\n"
            f"Responsible: {escape(task.responsible) if task.responsible else 'No responsible'}\n"
            f"Finished: {'Yes' if task.finished else 'No'}\n"
        )
        # Отправка сообщения
        await bot.send_message(chat_id=chat_id, text=message)