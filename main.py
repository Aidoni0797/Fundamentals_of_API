import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
import aiosqlite

TOKEN = "..."

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute('INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)',
                             (user_id, full_name, username))
        await connect.commit()
    await cursor.close()
    await connect.close()

@dp.message_handler(Command("start"))
async def start_command(message: types.Message) -> None:
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    await message.answer('Добро iDONi!')

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
