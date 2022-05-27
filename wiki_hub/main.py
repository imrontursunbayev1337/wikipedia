from aiogram import Bot, Dispatcher, executor, types
import wikipedia
import logging

token3 = '5370573759:AAG64APr_T6RR-2uweeeSba_FpEeiEVVSfM'
wikipedia.set_lang('uz')
bot = Bot(token=token3)
dispatcher = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dispatcher.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer("Assalomu aleykum! Botga hush kelibsiz")


@dispatcher.message_handler()
async def echo(receive: types.Message):
    try:
        data = wikipedia.summary(receive.text)
    except:
        data = 'Bunday maqola topilmadi!'
    await receive.reply(data)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
