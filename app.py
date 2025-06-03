import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Оплатил"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет! Это бот книги 'Бросаем курить вместе с ИИ'.

"
        "Чтобы получить книгу, сначала оплатите и нажмите кнопку 'Оплатил'.",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text.lower() == "оплатил")
async def send_book(message: types.Message):
    with open("book.pdf", "rb") as doc:
        await message.answer_document(doc, caption="📘 Вот ваша книга. Удачи!")