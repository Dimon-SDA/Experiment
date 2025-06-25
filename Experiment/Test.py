from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7565619095:AAHBlSa3i6Y25gGH78vKVeCYvMXZLwZWjAU'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет!\n\nЯ бот, демонстрирующий '
             'как работает разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/html - пример разметки с помощью HTML\n'
             '/markdownv2 - пример разметки с помощью MarkdownV2\n'
             '/noformat - пример с разметкой, но без указания '
             'параметра parse_mode\n'
             '/test1 - тестовый пример'
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Я бот, демонстрирующий '
             'как работает разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/html - пример разметки с помощью HTML\n'
             '/markdownv2 - пример разметки с помощью MarkdownV2\n'
             '/noformat - пример с разметкой, но без указания '
             'параметра parse_mode\n'
             '/test1 - тестовый пример\n'
             '/test3 - тестовый пример\n'
             '/test4 - тестовый пример\n'
             '/test6 - тестовый пример'
    )

# Этот хэндлер будет срабатывать на команду "/test"
@dp.message(Command(commands='test1'))
async def process_test1_command(message: Message):
    await bot.send_message(
        chat_id='1521587460',
        text='___Пример форматированного текста_\r__',
        parse_mode='HTML'
    )

@dp.message(Command(commands='test3'))
async def process_test3_command(message: Message):
    await bot.send_message(
        chat_id='1521587460',
        text='___Пример форматированного текста___',
        parse_mode='MarkdownV2'
    )

@dp.message(Command(commands='test4'))
async def process_test4_command(message: Message):
    await bot.send_message(
        chat_id='1521587460',
        text='<i><u>Пример форматированного текста</i></u>',
        parse_mode='HTML'
    )

@dp.message(Command(commands='test6'))
async def process_test6_command(message: Message):
    await bot.send_message(
        chat_id='1521587460',
        text='<ins><i>Пример форматированного текста</i></ins>',
        parse_mode='HTML'
    )

# Этот хэндлер будет срабатывать на команду "/html"
@dp.message(Command(commands='html'))
async def process_html_command(message: Message):
    await message.answer(
        text='Это текст, демонстрирующий '
             'как работает HTML-разметка:\n\n'
             '<b>Это жирный текст</b>\n'
             '<i>Это наклонный текст</i>\n'
             '<u>Это подчеркнутый текст</u>\n'
             '<span class="tg-spoiler">А это спойлер</span>\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help',
        parse_mode='HTML'
    )


# Этот хэндлер будет срабатывать на команду "/markdownv2"
@dp.message(Command(commands='markdownv2'))
async def process_markdownv2_command(message: Message):
    await message.answer(
        text='Это текст, демонстрирующий '
             'как работает MarkdownV2\-разметка:\n\n'
             '*Это жирный текст*\n'
             '_Это наклонный текст_\n'
             '__Это подчеркнутый текст__\n'
             '||А это спойлер||\n\n'
             'Чтобы еще раз посмотреть список доступных команд \- '
             'отправь команду /help',
        parse_mode='MarkdownV2'
    )


# Этот хэндлер будет срабатывать на команду "/noformat"
@dp.message(Command(commands='noformat'))
async def process_noformat_command(message: Message):
    await message.answer(
        text='Это текст, демонстрирующий '
             'как отображается текст, если не указать '
             'параметр parse_mode:\n\n'
             '<b>Это мог бы быть жирный текст</b>\n'
             '_Это мог бы быть наклонный текст_\n'
             '<u>Это мог бы быть подчеркнутый текст</u>\n'
             '||А это мог бы быть спойлер||\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help'
    )


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду\n\n'
             'Чтобы посмотреть список доступных команд - '
             'отправь команду /help'
    )


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)