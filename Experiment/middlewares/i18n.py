from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User


class TranslatorMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        user_lang = 'en'
        translations = data.get('_translations')
        print(user_lang)
        print(translations)

        i18n = translations.get(user_lang)
        print(i18n)
        if i18n is None:
            data['i18n'] = translations[translations['en']]
        else:
            data['i18n'] = i18n

        return await handler(event, data)
