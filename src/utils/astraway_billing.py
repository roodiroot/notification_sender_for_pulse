import asyncio
from datetime import datetime

from bot_instance import bot  # Импорт объекта bot
async def astraway_billing(chat_id) -> None:
    while True:
        # Получаем текущую дату и время
        now = datetime.now()

        # Проверяем, если сегодня 5-й или 10-й день месяца и время в интервале с 15:00 до 15:59
        if now.day == 8 and now.hour == 15:
            message = """
⚠️ Через 2 дня ваш аккаунт astraway.ru будет заблокирован.

Для продления работы необходимо пополнить баланс.
Детализация платежа

Стоимость услуг на период в 1 месяц.
Тарифный план: 550.00 руб.
            """
            await bot.send_message(chat_id=chat_id, text=message)

        # Ждем 1 час перед следующей проверкой
        await asyncio.sleep(3600)  # 3600 секунд = 1 час