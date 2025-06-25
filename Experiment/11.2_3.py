from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = '7565619095:AAHBlSa3i6Y25gGH78vKVeCYvMXZLwZWjAU'
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)


@dp.message()
async def receive_file_id(message: Message):
    if message.voice:
        print("voice_id", end=' - ')
        print(message.voice.file_id)

    elif message.photo:
        print("photo_id", end=' - ')
        print(message.photo[0].file_id)

    elif message.video:
        print("video_id", end=' - ')
        print(message.video.file_id)

    elif message.animation:
        print("animation_id", end=' - ')
        print(message.animation.file_id)

    elif message.document:
        print("document_id", end=' - ')
        print(message.document.file_id)

    elif message.audio:
        print("audio_id", end=' - ')
        print(message.audio.file_id)


if __name__ == '__main__':
    dp.run_polling(bot)