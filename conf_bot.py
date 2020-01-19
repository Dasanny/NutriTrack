# 826978167:AAFIkxM6InqxRDT5R3GOyEnTAKFA3YzMQTo
lstr = '''
Good'''

hello = '''
Hello!

I am a NutritionBot®️.

You can easily calcilate nutrition via, just send me a photo of your meal or write it to me. 
Also I recognizing voice massages, so just say me what you are eating!☑️

Let's start👇
'''
import telebot
import urllib
import time
from telebot import types

token = '983432742:AAEDA4z6vhGV0VTPpfUXDw_ZZyKhdY5UGUw'
bot = telebot.TeleBot(token, threaded=False)
admin = []
users = []

print('starting...')
photos = [
          ['name\ncharacteristics', 'http://www.sovel.org/images/upload/ru/71/Nikeev_300400.jpg'],
          ['Игорь Смирнов\nКоммерческий директор, ООО "Остек-Электро"', 'http://www.sovel.org/images/upload/ru/71/Smirnov_300h400.jpg'],
          ['Виктор Ваньков\nНачальник отдела разработки систем в корпусе, АО "ПКК Миландр"', 'http://www.sovel.org/images/upload/ru/71/Vankov_300h400.jpg'],
          ['Сергей Тимошенков\nДоктор технических наук, профессор, директор Института нано- и микросистемной техники, МИЭТ', 'http://www.sovel.org/images/upload/ru/71/Timoshenkov300H4001.jpg'],
          ['Денис Вертянов\nРуководитель Учебно-научного центра проектирования Mentor Graphics, Институт нано- и микросистемной техники, МИЭТ', 'http://www.sovel.org/images/upload/ru/71/Vertyanov300H400.jpg'],
          ['Алексей Решетников\nГенеральный директор, Engineering Solutions,Ltd', 'http://www.sovel.org/images/upload/ru/71/Reshetnikov_300h400.jpg'],
          ['Сергей Доровских\nГлавный технолог, АО "Микроволновые системы"', 'http://www.sovel.org/images/upload/ru/71/Dorovskih_300400.jpg'],
          ['Сергей Чигиринский\nТехнический директор, к.ф.-м.н., ООО "АК Микротех"', 'http://www.sovel.org/images/upload/ru/71/Chigirinsky_300h400.jpg'],
          ['Михаил Чувствин\nНачальник опытно-конструкторского отдела, GS Nanotech"', 'http://www.sovel.org/images/upload/ru/71/Chuvstvin_300H400.jpg'],
          ['Иван Селиванов\nВедущий специалист, АО МЕГРАТЕК', 'http://www.sovel.org/images/upload/ru/71/Selivanov_300h400.jpg'],
          ['Сергей Беляков\nРуководитель отдела маркетинга и продвижения, GS Nanotech', 'http://www.sovel.org/images/upload/ru/71/Belyakov_300400.png'],
          ['Владимир Бутузов\nВедущий разработчик ИС и СнК,к.т.н., ООО "ОКБ Пятое Поколение', 'http://www.sovel.org/images/upload/ru/71/Butuzov300h400.jpg'],
          ['Владимир Косевской\nДиректор по производству, АО "НПЦ СпецЭлектронСистемы"', 'http://www.sovel.org/images/upload/ru/71/Kosevskoy300h4001.jpg'],
          ['Максим Савицкий\nВедущий инженер-конструктор многокристальных модулей, GS Nanotech', 'http://www.sovel.org/images/upload/ru/71/Savickiy300h400.jpg'],
          ['Алексей Болебрух\nВедущий инженер-тестировщик, GS Nanotech', 'http://www.sovel.org/images/upload/ru/71/Bolebruh300h400.jpg'],
          ['Константин Белов\nГлавный технолог, GS Nanotech', 'http://www.sovel.org/images/upload/ru/71/Belov_300h400..jpg'],
          ['Игорь Беляков\nАспирант, Институт нано- и микросистемной техники, МИЭТ', 'http://www.sovel.org/images/upload/ru/71/300H400_d.jpg'],
          ['Андрей Скворцов\nИнженер, Keysight Technologies', 'http://www.sovel.org/images/upload/ru/71/300H400_d.jpg']
         ]

states = ['Write your full name👇',
          'Write you age👇',
          'How many callories you want to eat during a day👇',
          'Write alergic products👇',
          'Write your diet👇',
          'Write your gender👇',
          'You are already registred👇']

def pdf(call):
    print(call.message.chat.id)
    if call.data == 'PDFyes':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="http://www.sovel.org/images/upload/ru/1565/ProgramSIP_28032019.pdf")
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="хорошо")    

def mentors(call):
    print(call.message.chat.id)
    

    if len(call.data) == 5:
        index = int(call.data[-1])
    else:
        index = int(call.data[-2:])

    if 'left' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        if index == 0:
            index = 18

        keyboard = types.InlineKeyboardMarkup()
        left = types.InlineKeyboardButton(text='<', callback_data='left'+str(index-1))
        right = types.InlineKeyboardButton(text='>', callback_data='righ'+str(index-1))
        keyboard.add(left, right)

        bot.send_photo(call.message.chat.id, urllib.request.urlopen(photos[index-1][1]).read(), photos[index-1][0], reply_markup=keyboard)
    if 'righ' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        if index == 17:
            index = -1

        keyboard = types.InlineKeyboardMarkup()
        left = types.InlineKeyboardButton(text='<', callback_data='left'+str(index+1))
        right = types.InlineKeyboardButton(text='>', callback_data='righ'+str(index+1))
        keyboard.add(left, right)

        bot.send_photo(call.message.chat.id, urllib.request.urlopen(photos[index+1][1]).read(), photos[index+1][0], reply_markup=keyboard)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    global users
    users.append(message.chat.id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    strategy = types.KeyboardButton('Send a meal')
    speakers = types.KeyboardButton('Calories in products')
    place = types.KeyboardButton('Calculate calories')
    rules = types.KeyboardButton('Write what you are eating')
    registration = types.KeyboardButton('Registration')
    
    markup.row(strategy, speakers)
    markup.row(place, rules)
    markup.row(registration)

    bot.send_message(message.chat.id, hello, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == 'Send a meal')
def strategy(message):
    print(message.chat.id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Male', callback_data='PDFyes'))
    keyboard.add(types.InlineKeyboardButton(text='Female', callback_data='PDFno'))

    bot.send_message(message.chat.id, "Send me a photo of what you are eating and I will calculate how many calories in it", reply_markup=keyboard)

@bot.message_handler(func=lambda msg: msg.text == 'Calculate calories')
def place(message):
    print(message.chat.id) 
    bot.send_message(message.chat.id, "Место проведения: г. Москва, бизнес-отель «Бородино», ул. Русаковская, дом 13, строение 5, 3 этаж, зал \"Ермолов-Тучков\". ")
    bot.send_location(message.chat.id, '55.784587', '37.672109')

@bot.message_handler(func=lambda msg: msg.text == 'Write what you are eating')
def rules(message):
    print(message.chat.id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Карточка организатора', callback_data='card'))
    keyboard.add(types.InlineKeyboardButton(text='Оплатить сейчас', callback_data='pay'))
    keyboard.add(types.InlineKeyboardButton(text='Телефон для справок', callback_data='phone'))

    bot.send_message(message.chat.id, lstr, reply_markup=keyboard)

@bot.message_handler(func=lambda msg: msg.text == 'Calories in products')
def speakers(message):
    print('------*******--------')
    print(message.chat.id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='<', callback_data='left0'), types.InlineKeyboardButton(text='>', callback_data='righ0'))

    bot.send_photo(message.chat.id, urllib.request.urlopen(photos[0][1]).read(), photos[0][0], reply_markup=keyboard)

@bot.message_handler(func=lambda msg: msg.text == 'Registration')
def registration(message):
    file = open('data.txt', 'r')
    data = eval(file.read())
    file.close()

    if not message.chat.id in data:
        data[message.chat.id] = {'state': 0, 'name': None, 'fio': None, 'dolg': None, 'email': None, 'phone': None, 'money': None, 'payd': None}
    
    bot.send_message(message.chat.id, states[data[message.chat.id]['state']])
    
    file = open('data.txt', 'w')
    file.write(str(data))
    file.close()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data in ['PDFno', 'PDFyes']:
        pdf(call)
    if 'righ' in call.data or 'left' in call.data:
        print(call.data)
        mentors(call)
    if call.data == 'card':
        bot.send_message(call.message.chat.id, 'https://vk.com/doc226618405_496269466?hash=86ead02baa7dda57a1&dl=42c2c96915501ec7ab')
    if call.data == 'pay':
        bot.send_message(call.message.chat.id, 'Пожалуйста, произведите оплату через Яндекс кассу в размере 12 500 рублей')
        bot.send_invoice(call.message.chat.id, title='Оплата',
                                               description='оплатите:',
                                               provider_token='381764678:TEST:9078',
                                               currency='RUB',
                                               start_parameter='test',
                                               invoice_payload='OUOUOU',
                                               prices=[types.LabeledPrice(amount=6500, label=' рублей ')]
                                               )
    if call.data == 'phone':
        bot.send_message(call.message.chat.id, '+7(916)917-16-11, +7(495)280-04-19')
    if call.data in ['cardYes', 'cardNo']:
        file = open('data.txt', 'r')
        data = eval(file.read())
        file.close()
        print(data)

        if data[call.message.chat.id]['state'] == 5:
            data[call.message.chat.id]['money'] = call.data
            data[call.message.chat.id]['state'] += 1

            if call.data == 'cardYes':
                bot.send_message(call.message.chat.id, 'Загрузите карточку предприятия ')
            elif call.data == 'cardNo':
                bot.send_message(call.message.chat.id, 'Your are successfully registred! ')
                for a in admin:
                    bot.send_message(a, str(data[call.message.chat.id]))

            file = open('data.txt', 'w')
            file.write(str(data))
            file.close()

@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    print('check')
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials, try to pay again in a few minutes, we need a small rest.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    print('nice')
    file = open('data.txt', 'r')
    data = eval(file.read())
    file.close()

    data[message.chat.id]['paid'] = 'yes'

    file = open('data.txt', 'w')
    file.write(str(data))
    file.close()
    bot.send_message(message.chat.id, 'Спасибо за оплату', parse_mode='Markdown')

@bot.message_handler(content_types=['document'])
def card(message):
    file = open('data.txt', 'r')
    data = eval(file.read())
    file.close()
    print(data)

    if message.chat.id in data:
        if data[message.chat.id]['state'] == 6:
            try:
                chat_id = message.chat.id
           
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
              
                src = str(chat_id) + message.document.file_name
                with open(src, 'wb') as new_file:
                   new_file.write(downloaded_file)

                bot.send_message(message.chat.id, 'Photo was successfully uploaded.\n You will have got your report shortly.')
                for a in admin:
                    bot.send_message(a, str(data[call.message.chat.id]))
            except Exception as e:
                bot.send_message(message.chat.id, str(e))


@bot.message_handler()
def all(message):
    print('-----------------{}--------------------'.format(len(users)))
    file = open('data.txt', 'r')
    data = eval(file.read())
    file.close()
    print(data)

    if message.text == 'iwishihaveanadmin':
        global admin
        if not message.chat.id in admin:
            admin.append(message.chat.id)
    elif message.chat.id in data:
        if data[message.chat.id]['state'] == 0:
            data[message.chat.id]['name'] = message.text
            data[message.chat.id]['state'] += 1
            bot.send_message(message.chat.id, states[data[message.chat.id]['state']])
        elif data[message.chat.id]['state'] == 1:
            data[message.chat.id]['fio'] = message.text
            data[message.chat.id]['state'] += 1
            bot.send_message(message.chat.id, states[data[message.chat.id]['state']])
        elif data[message.chat.id]['state'] == 2:
            data[message.chat.id]['dolg'] = message.text
            data[message.chat.id]['state'] += 1
            bot.send_message(message.chat.id, states[data[message.chat.id]['state']])    
        elif data[message.chat.id]['state'] == 3:
            data[message.chat.id]['email'] = message.text
            data[message.chat.id]['state'] += 1
            bot.send_message(message.chat.id, states[data[message.chat.id]['state']])
        elif data[message.chat.id]['state'] == 4:
            data[message.chat.id]['phone'] = message.text
            data[message.chat.id]['state'] += 1

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text='Male', callback_data='cardYes'), types.InlineKeyboardButton(text='Female', callback_data='cardNo'))
            bot.send_message(message.chat.id, states[data[message.chat.id]['state']], reply_markup=keyboard)
        elif message.chat.id in admin:
            for u in users:
                bot.send_message(u, message.text)
        
        file = open('data.txt', 'w')
        file.write(str(data))
        file.close()
    else:
        for a in admin:
            bot.send_message(a, message.text)

        print('wtf?', message.text)

    print(data)

while True:
    try:
        bot.polling()    
    except:
        time.sleep(2)
    print('lol')
    time.sleep(2)
    
        
