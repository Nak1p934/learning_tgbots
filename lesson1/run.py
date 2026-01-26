from aiogram import Dispatcher, Bot
from BOTTOKEN_LESS1 import TOKEN1
import asyncio
from routes_for_lesson1 import router_less1


async def main():
    dp = Dispatcher()
    bot = Bot(token=TOKEN1)
    dp.include_router(router_less1)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main()) 
    except:
        print("Завершение работы")