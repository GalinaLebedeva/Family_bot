import config
import utilite
import callback
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from utilite import Data_Base_var


async def main():
  # Включаем логирование, чтобы не пропустить важные сообщения
  logging.basicConfig(level=logging.DEBUG)
  # Объект бота
  bot = Bot(token=config.TOKEN)
  # Диспетчер
  dp = Dispatcher()
  # Хэндлер на команду /start
  dp.message.register(utilite.cmd_start, Command(commands=["start"]))
  dp.callback_query.register(callback.call_cancel, F.data == 'cancel')
  dp.callback_query.register(callback.call_start, F.data.startswith('start_'))
  dp.callback_query.register(callback.call_category, F.data.startswith('category_'))
  dp.callback_query.register(callback.call_date, F.data.startswith('date_'))
  dp.message.register(utilite.get_date, Data_Base_var.summa)

  # dp.callback_query.register(utilite, F.data == 'cancel')


  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
