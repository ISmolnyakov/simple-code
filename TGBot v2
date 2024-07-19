import random
from io import StringIO

from telebot import TeleBot, types, formatting
from telebot import custom_filters

import config
import jokes
import messages
import my_filters

token = config.bot_token
bot = TeleBot(token)
bot.add_custom_filter(custom_filters.TextMatchFilter())
# bot.add_custom_filter(custom_filters.TextContainsFilter())
bot.add_custom_filter(custom_filters.ForwardFilter())
bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(my_filters.IsBotAdmin())
bot.add_custom_filter(my_filters.ContainWord())


@bot.message_handler(commands=['start'])
def reply_to_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.welcome
    )


@bot.message_handler(commands=['help'])
def reply_to_help(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.help_menu
    )


@bot.message_handler(commands=['joke'])
def send_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        formatting.hcite(jokes.get_rand_joke_text()),
        parse_mode='HTML'
    )


@bot.message_handler(commands=['joke2'])
def send_two_part_joke(message: types.Message):
    setup, delivery = jokes.get_two_part_joke()
    j_text = formatting.format_text(
        formatting.escape_html(setup),
        formatting.hspoiler(delivery)
    )
    bot.send_message(
        message.chat.id,
        j_text,
        parse_mode='HTML'
    )


@bot.message_handler(commands=['dogs'])
def send_dogs(message: types.Message):
    bot.send_photo(
        message.chat.id,
        config.photo_url,
        'Here is a power dog to you!',
        reply_to_message_id=message.id
    )


@bot.message_handler(commands=['spaceman'])
def send_spaceman(message: types.Message):
    bot.send_photo(
        message.chat.id,
        config.spaceman_pic_url
    )


@bot.message_handler(commands=['spaceman_file'])
def send_spaceman_file(message: types.Message):
    photo_file = types.InputFile(config.spaceman_pic_file)
    bot.send_document(
        message.chat.id,
        photo_file
    )


@bot.message_handler(commands=['me'])
def send_my_info(message: types.Message):
    data = StringIO()
    data.write(f'Ваше username:{message.from_user.username}\n')
    data.write(f'Ваше полное имя: {message.from_user.full_name}\n')
    data.write(f'Ваш ID: {message.from_user.id}\n')
    data.seek(0)
    bot.send_document(
        message.chat.id,
        types.InputFile(data),
        visible_file_name='your-info.txt',
        caption=messages.your_info

    )


@bot.message_handler(commands=['chat_id'])
def show_chat_id(message: types.Message):
    bot.send_message(
        message.chat.id,
        f"{message.chat.id}"
    )


@bot.message_handler(commands=['secret'], is_bot_admin=True)
def tell_a_secret(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=messages.admin_msg
    )


@bot.message_handler(commands=['secret'], is_bot_admin=False)
def keep_this_secret(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=messages.not_admin_msg
    )


@bot.message_handler(content_types=['sticker'])
def reply_to_sticker(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Шикарный стикер пак!!!',
        reply_to_message_id=message.id
    )


@bot.message_handler(content_types=['animation'])
def reply_to_gif(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Обожаю гифки!',
        reply_to_message_id=message.id
    )


def cats_in_caption_check(message: types.Message):
    return message.caption and 'кот' in message.caption.lower()


@bot.message_handler(contain_word="кот")
def no_cats_allowed(message: types.Message):
    bot.send_message(
        message.chat.id,
        "NO CATS ALLOWED!"
    )


@bot.message_handler(content_types=['photo'], func=cats_in_caption_check)
def send_reply_to_cats(message: types.Message):
    if cats_in_caption_check:
        bot.send_message(
            message.chat.id,
            'Шикарный котик!',
            reply_to_message_id=message.message_id
        )
    else:
        photo_file_id = message.photo[-1].file_id
        bot.send_photo(
            message.chat.id,
            photo_file_id,
            reply_to_message_id=message.message_id
        )


@bot.message_handler(content_types=['photo'])
def send_photo_reply(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    if message.caption:
        bot.send_photo(
            message.chat.id,
            photo_file_id,
            caption='Крутое фото!',
            reply_to_message_id=message.message_id
        )
    else:
        bot.send_photo(
            message.chat.id,
            photo_file_id,
            reply_to_message_id=message.message_id
        )


@bot.message_handler(commands=['photofile'])
def send_photo_file(message: types.Message):
    photo_file = types.InputFile('pics/simple ghost eating ice cream doodle png white bac.webp')
    bot.send_photo(
        message.chat.id,
        photo_file
    )


@bot.message_handler(commands=['doc'])
def send_doc(message: types.Message):
    photo_file = types.InputFile('pics/msg379668733-113514.jpg')
    bot.send_document(
        message.chat.id,
        photo_file
    )


@bot.message_handler(commands=['document'])
def send_document(message: types.Message):
    bot.send_document(
        message.chat.id,
        document=types.InputFile('text.txt')
    )


@bot.message_handler(commands=['gen_txt'], is_forwarded=True)
def no_forward(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.dont_forward_commands,
    )


@bot.message_handler(commands=['gen_txt'])
def send_generated_txt(message: types.Message):
    file = StringIO()
    file.write("Your random number: ")
    file.write(str(random.randint(a=1, b=100)))
    file.seek(0)
    gen = types.InputFile(file)
    bot.send_document(
        message.chat.id,
        document=gen,
        visible_file_name="Your random number.txt"
    )


def is_hi(message: types.Message):
    return message.text and "привет" in message.text.lower()


@bot.message_handler(text=custom_filters.TextFilter(
    contains=["погода"], ignore_case=True))
def weather(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Nice weather'
    )


@bot.message_handler(func=is_hi)
def reply_to_hi(message: types.Message):
    bot.send_message(
        message.chat.id,
        'Greetings!'
    )


@bot.message_handler(is_reply=True)
def reply(message: types.Message):
    msg_type = message.reply_to_message.content_type
    if msg_type in config.content_types:
        msg_type = config.content_types[msg_type]
    bot.send_message(
        message.chat.id,
        f'You replied to {msg_type}',
        reply_to_message_id=message.reply_to_message.message_id
    )


@bot.message_handler()
def copy_message(message: types.Message):
    bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.id
    )


@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    text_lower = text.lower()
    if 'как дела' in text_lower:
        bot.send_message(
            message.chat.id,
            messages.how
        )
    elif 'пока' in text_lower or 'до свидания' in text_lower:
        bot.send_message(
            message.chat.id,
            messages.bb
        )
    else:
        bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
