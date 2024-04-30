import asyncio

from aiogram import Bot, Dispatcher
from hendlers import user_hendlers

BOT_TOKEN = 'TOKEN'


async def main():

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_hendlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
