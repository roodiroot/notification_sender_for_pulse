from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot_instance import dp
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Enter this ID {html.bold(message.chat.id)} in the Pulse settings.")