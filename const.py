import os

import django
from telebot import types, TeleBot

import buttons

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BukBot.settings')
django.setup()

from app.models import Text, User

BOT_TOKEN = '7195501588:AAEVSKvVeH9JNg9FXiZ8iph1ryAdeSWX4p8'

bot = TeleBot(BOT_TOKEN)
def get_enteties(a):
    entities = []
    for entity in a.split('|')[:-1]:
        n = eval(entity)
        entities.append(
            types.MessageEntity(type=n['type'], offset=n['offset'], length=n['length'], url=n['url'],
                                language=n['language'], custom_emoji_id=n['custom_emoji_id']))
    return entities
def text(param, chat_id, markup=None):
    global_text, _ = Text.objects.get_or_create(id=1)
    params = getattr(global_text, param).split('\t\t\t')
    ln = len(params)
    user = User.objects.get(chat_id=chat_id)
    if user.is_admin:
        markup = buttons.edit_text(markup=markup, param=param)
    text = params[0]
    type = 'text'
    entities = []
    media = None
    if ln == 2:
        entities = get_enteties(params[1])
    elif ln == 3:
        type = 'photo'
        entities = get_enteties(params[1])
        media = params[2]
    if type == 'text':
        bot.send_message(chat_id=chat_id, text=text, entities=entities, reply_markup=markup)
    elif type == 'photo':
        try:
            bot.send_photo(chat_id=chat_id, photo=media, caption=text, caption_entities=entities, reply_markup=markup)
        except Exception as ex:
            bot.send_message(chat_id=chat_id, text='Главное меню', reply_markup=markup)
