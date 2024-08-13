from telebot import types


def menu():
    markup = types.InlineKeyboardMarkup()
    webapp = types.WebAppInfo(url='https://nearby-cheetah-patient.ngrok-free.app/')
    button = types.InlineKeyboardButton('Топ букмекеров', web_app=webapp)
    markup.add(button)
    return markup


def edit_text(markup, param):
    edit = types.InlineKeyboardButton(text='Изменить текст', callback_data=f'edit_text|{param}')
    send_mail = types.InlineKeyboardButton('Сделать рассылку', callback_data='send_mail')
    markup.add(send_mail, edit)
    return markup
