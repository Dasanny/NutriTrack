# 826978167:AAFIkxM6InqxRDT5R3GOyEnTAKFA3YzMQTo
lstr = '''
Good'''

hello = '''
Hello!

I am NutritionBot®️.

You can easily calculate nutrition by sending me a photo of your meal or texting me.
I also recognize voice messages, so just say what you are eating!☑️

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

["Rice\n","Amount: 100 grams","Calories: 130","Total fat (g): 0.9","Cholesterol (mg): 0","Protein (g): 2.6","Sodium (mg): 5", "Iron (%): 2","https://hips.hearstapps.com/vidthumb/images/delish-u-rice-2-1529079587.jpg"],
["Chicken\n","Amount: 100 grams","Calories: 239","Total fat (g): 14","Cholesterol (mg): 88","Protein (g): 27","Sodium (mg): 82", "Iron (%): 7","https://www.maangchi.com/wp-content/uploads/2018/02/roasted-chicken-1.jpg"],
["Beef\n","Amount: 100 grams","Calories: 250","Total fat (g): 15","Cholesterol (mg): 90","Protein (g): 26","Sodium (mg): 72", "Iron (%): 14","https://www.pressurecookrecipes.com/wp-content/uploads/2019/11/instant-pot-roast-beef.jpg"],
["Pork\n","Amount: 100 grams","Calories: 145","Total fat (g): 14","Cholesterol (mg): 80","Protein (g): 27","Sodium (mg): 62", "Iron (%): 4","https://www.thespruceeats.com/thmb/csX1Y5mVIaiMXV4-uFN976C9Eds=/2048x1152/smart/filters:no_upscale()/garlic-and-herb-crusted-pork-loin-roast-3059504-7_preview-5b2bc4f88023b90037a968fa.jpg"],
["Apple\n","Amount: 100 grams","Calories: 52","Total fat (g): 0.2","Cholesterol (mg): 0","Protein (g): 0.3","Sodium (mg): 1", "Iron (%): 0","https://www.allfoodsinfo.com/wp-content/uploads/2019/08/apple-benefits-vegetable-1080x540.jpg"],
["Banana\n","Amount: 100 grams","Calories: 89","Total fat (g): 0.3","Cholesterol (mg): 0","Protein (g): 1.1","Sodium (mg): 1", "Iron (%): 1","https://api.time.com/wp-content/uploads/2019/11/gettyimages-459761948.jpg?w=600&quality=85"],
["Orange\n","Amount: 100 grams","Calories: 47","Total fat (g): 0.1","Cholesterol (mg): 0","Protein (g): 0.9","Sodium (mg): 0", "Iron (%): 0","https://i5.walmartimages.ca/images/Enlarge/110/004/999999-33383110004.jpg"],
["Broccoli\n","Amount: 100 grams","Calories: 31","Total fat (g): 0.4","Cholesterol (mg): 0","Protein (g): 2.5","Sodium (mg): 33", "Iron (%): 3","https://az836796.vo.msecnd.net/media/image/product/fr/medium/0000000094060.jpg"],
["Carrot\n","Amount: 100 grams","Calories: 41","Total fat (g): 0.2","Cholesterol (mg): 0","Protein (g): 0.9","Sodium (mg): 69", "Iron (%): 4","https://www.almanac.com/sites/default/files/image_nodes/carrots-table_popidar-ss.jpg"],
["White Bread\n","Amount: 100 grams","Calories: 265","Total fat (g): 3.2","Cholesterol (mg): 0","Protein (g): 9","Sodium (mg): 491", "Iron (%): 19","https://images.smuckers.ca/images/recipes/29/Basic-White-Bread_desktop.jpg"],

]
states = ['Enter your full name👇',
          'Enter your age👇',
          'How many calories are you planning on consuming today?👇',
          'Enter your allergies👇',
          'Enter your gender👇',
          'You are already registered👇']

def pdf(call):
    print(call.message.chat.id)
    if call.data == 'PDFyes':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="y")
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="n")

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

    bot.send_message(message.chat.id, "Send me a photo of what you are eating and I will calculate how many its calories", reply_markup=keyboard)

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
