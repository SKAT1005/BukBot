import os
import threading

import django
from telebot import TeleBot

import buttons
from const import text

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BukBot.settings')
django.setup()
from app.models import User, Text

bot = TeleBot('7195501588:AAEVSKvVeH9JNg9FXiZ8iph1ryAdeSWX4p8')
Text.objects.get_or_create(id=1)


def edit_text(chat_id, user, action, message):
    b = True
    global_text, _ = Text.objects.get_or_create(id=1)
    if message.content_type == 'text':
        text = message.text
        a = message.entities
        n = ''
        if a:
            for i in a:
                n += f'{i}|'
            text += f'\t\t\t{n}'

    elif message.content_type == 'photo':
        a = message.caption_entities
        text = message.caption
        n = ''
        if a:
            for i in a:
                n += f'{i}|'
            text += f'\t\t\t{n}'
        media = message.photo[0].file_id
        if media:
            text += f'\t\t\t{media}'
    else:
        bot.send_message(chat_id=chat_id, text='Отправлять можно только текст и фотографии')
        b = False
    if b:
        setattr(global_text, action, text)
        user.action = ''
        user.save()
        global_text.save()
        menu(chat_id=chat_id)



def menu(chat_id):
    text(param='menu', markup=buttons.menu(), chat_id=chat_id)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    User.objects.get_or_create(chat_id=chat_id)
    menu(chat_id=chat_id)


def run_server():
    os.system(
        'ngrok config add-authtoken 2euPY6ANjVpzT2UxRxys9yQOR7B_7VvCrayL4A2N7HoLqy4Mf & ngrok http --domain=nearby-cheetah-patient.ngrok-free.app 127.0.0.1:8000')

@bot.message_handler(content_types=['text', 'video', 'photo'])
def get_message(message):
    chat_id = message.chat.id
    user = User.objects.get(chat_id=chat_id)
    action = user.action.split('|')
    if action[0] == 'edit_text':
        edit_text(chat_id=chat_id, user=user, action=action[1], message=message)
def send_mail(message, chat_id):
    text = message.text
    entities = message.entities
    users = User.objects.all()
    for user in users:
        try:
            bot.send_message(chat_id=user.chat_id, text=text, entities=entities)
        except Exception:
            pass
    bot.send_message(chat_id=chat_id, text='Рассылка успешно отправлена всем пользователям')
    menu(chat_id=chat_id)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    message_id = call.message.id
    chat_id = call.message.chat.id
    user, _ = User.objects.get_or_create(chat_id=call.from_user.id)
    if call.message:
        data = call.data.split('|')
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception:
            pass
        if data[0] == 'edit_text':
            user.action = f"edit_text|{data[1]}"
            user.save()
        elif data[0] == 'send_mail':
            msg = bot.send_message(chat_id=chat_id, text='Введите сообщение для рассылки')
            bot.register_next_step_handler(msg, send_mail, chat_id)


if __name__ == '__main__':
    # update_code = threading.Thread(target=run_server)
    # update_code.start()
    bot.polling(none_stop=True)
