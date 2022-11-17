import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import CommandStart
from config import API_TOKEN
from aiogram import types

bot = Bot(token=API_TOKEN, parse_mode="HTML")
db = Dispatcher (bot=bot)


logging.basicConfig(level=logging.DEBUG)

@db.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        text=f"👋 Hi {message.from_user.full_name}\n\n"
        + f"🆔 User ID: {message.from_user.id}\n"
        + f"👦🏻 First name: {message.chat.first_name}\n"
        + f"🔹 Last name: {message.chat.last_name}\n"
        + f"📎 Username: {message.chat.username}\n"

    )

    

@db.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(text="👨🏻‍💻 Admin: @thebest_coder")



@db.message_handler()
async def help(message: types.Message):
    await message.answer(
        text=f"{message.chat.first_name} xabar yubordingiz 🌚"
        )





if __name__ == "__main__":
    executor.start_polling(dispatcher=db)