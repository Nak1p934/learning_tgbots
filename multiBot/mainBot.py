from aiogram import Dispatcher, Bot
from multiBot.BOTTOKEN import TOKEN
import asyncio
from multiBot.routes import router


async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main()) 
    except:
        print("Завершение работы")