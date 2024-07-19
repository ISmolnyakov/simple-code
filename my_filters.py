from telebot.types import Message
from telebot.custom_filters import (SimpleCustomFilter, AdvancedCustomFilter)
import config


class IsBotAdmin(SimpleCustomFilter):
    key = "is_bot_admin"

    def check(self, message: Message):
        return message.from_user.id in config.chat_admin


class ContainWord(AdvancedCustomFilter):
    key = "contain_word"

    def check(self, message: Message, word: str):
        text = message.text or message.caption
        if not text:
            return False

        return word in text.lower()
