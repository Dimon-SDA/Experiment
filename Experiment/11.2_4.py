from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaVideo, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7565619095:AAHBlSa3i6Y25gGH78vKVeCYvMXZLwZWjAU'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAICEGhZdueZ7tniTlU8vgqLv_L7w7XgAAJV8TEb07HQShTNybE6oJ1jAQADAgADcwADNgQ',
    'photo_id2': 'AgACAgIAAxkBAAICEWhZdxq9XNDGzsT4c3d3lPtg8NgdAAJW8TEb07HQStSQve61qbWYAQADAgADcwADNgQ',
    'voice_id1': 'AwACAgIAAxkBAAICGWhZefOwaWGWCIFXF1RWWB9usqJ5AAI4dgAC07HQSpKn9H95IcnbNgQ',
    'voice_id2': 'AwACAgIAAxkBAAICGmhZegABXDoZ3XysVBvMLdfFId6FEwACOXYAAtOx0ErX5xMB4K_XdjYE',
    'audio_id1': 'CQACAgIAAxkBAAICEmhZd5VFom4pzpfriH-C42sEmwg4AAIMdgAC07HQSk_NF3RTA1fONgQ',
    'audio_id2': 'CQACAgIAAxkBAAICE2hZd-9kXO_RiHWze2lqShdNmktDAAIRdgAC07HQSnpOUAM9VBioNgQ',
    'document_id1': 'BQACAgIAAxkBAAICFGhZeBCjAZdDk1BlC4BVrVy-Ks8DAAKhewACNgTRShqv4MV_vE-VNgQ',
    'document_id2': 'BQACAgIAAxkBAAICFWhZeEIa660vUibhBfx52SX79aV0AAIYdgAC07HQSl5k8BiAK10eNgQ',
    'video_id1': 'BAACAgIAAxkBAAICFmhZeLO5FOPk734mvALfLxml3_EZAAIfdgAC07HQSv6zqFk3GcZkNgQ',
    'video_id2': 'BAACAgIAAxkBAAICGGhZedfw1tTiY05u-PbUk6ew9GcuAAI2dgAC07HQSklQe9UhC-CJNgQ',
}


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'photo')
    await message.answer_document(
        document=LEXICON['video_id1'],
        caption='Это video 1',
        reply_markup=markup
    )


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(F.data.in_(
    ['text', 'audio', 'video', 'document', 'photo', 'voice']
))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=LEXICON['photo_id2'],
                caption='Это photo 2'
            ),
            reply_markup=markup
        )
    except TelegramBadRequest:
        markup = get_markup(2, 'photo')
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=LEXICON['video_id1'],
                caption='Это video 1'
            ),
            reply_markup=markup
        )


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    # Удаляем сообщение пользователя
    await message.delete()
    
    await message.answer(text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
