import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO, filename='logs.txt', format="%(asctime)s %(levelname)s %(message)s)")
logging.getLogger().addHandler(logging.StreamHandler())  # логгирование в консоль
# Объект бота
bot = Bot(token="5553234170:AAHha16L5V3RiC-MbD-F0Df01hNZ6orMlXY")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
