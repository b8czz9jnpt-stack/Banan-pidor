import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message()
async def handle_message(message: types.Message):
    if message.text and message.text.lower().strip() == "лосось пидорша":
        await message.answer("сам ты пидор")


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
