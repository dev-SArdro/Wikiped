import wikipedia

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API_TOKEN = '5103260932:AAErH9lf7X2EDV_B1SEHAGM9S6aQGUlWTIg'
wikipedia.set_lang('uz')
inline_btn_1 = InlineKeyboardButton('Saytdan_qidirish', callback_data='button1', url="https://www.wikipedia.org/")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalom alekum Wikipedia botiga\n"
                        "xush kelibsiz."
                        "O'zingizga kerakli Malumotni\n"
                        "Qidirishingizda biz yordam\n"
                        "beramiz <b>Kutubxona</b> www.wikipedia.org", parse_mode="HTML")


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond, reply_markup=inline_kb1)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!", )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
