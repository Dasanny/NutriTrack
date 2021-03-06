lstr = '''
Choose your preferences'''

hello = '''
Hello!

I am a NutritionBot®️.

You can easily calculate nutrition with me, just send me a photo of your meal or text it to me.
Also I recognize voice messages, so just tell me what you are eating!☑️

Let's start👇
'''
import telebot
import urllib
import time
from telebot import types

#token = 'private'
bot = telebot.TeleBot(token, threaded=False)
admin = []
users = []

print('starting...')
photos = [
          ['Rice\n","Amount: 100 grams","Calories: 130","Total fat (g): 0.9","Cholesterol (mg): 0","Protein (g): 2.6","Sodium (mg): 5", "Iron (%): 2', 'https://static01.nyt.com/images/2018/02/21/dining/00RICEGUIDE8/00RICEGUIDE8-articleLarge.jpg'],
          ['Chicken\n","Amount: 100 grams","Calories: 239","Total fat (g): 14","Cholesterol (mg): 88","Protein (g): 27","Sodium (mg): 82", "Iron (%): 7', 'https://s23209.pcdn.co/wp-content/uploads/2019/01/Instant-Pot-Rotisserie-ChickenIMG_8266.jpg'],
          ['Beef\n","Amount: 100 grams","Calories: 250","Total fat (g): 15","Cholesterol (mg): 90","Protein (g): 26","Sodium (mg): 72", "Iron (%): 14', 'https://www.pressurecookrecipes.com/wp-content/uploads/2019/11/instant-pot-roast-beef.jpg'],
          ['Pork\n","Amount: 100 grams","Calories: 145","Total fat (g): 14","Cholesterol (mg): 80","Protein (g): 27","Sodium (mg): 62", "Iron (%): 4', 'https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/roast-rack-of-pork-with-wild-garlic-stuffing_1.jpg'],
          ['Apple\n","Amount: 100 grams","Calories: 52","Total fat (g): 0.2","Cholesterol (mg): 0","Protein (g): 0.3","Sodium (mg): 1", "Iron (%): 0', 'https://i5.walmartimages.ca/images/Large/094/514/6000200094514.jpg'],
          ['Banana\n","Amount: 100 grams","Calories: 89","Total fat (g): 0.3","Cholesterol (mg): 0","Protein (g): 1.1","Sodium (mg): 1", "Iron (%): 1', 'https://api.time.com/wp-content/uploads/2019/11/gettyimages-459761948.jpg?w=600&quality=85'],
          ['Orange\n","Amount: 100 grams","Calories: 47","Total fat (g): 0.1","Cholesterol (mg): 0","Protein (g): 0.9","Sodium (mg): 0", "Iron (%): 0', 'https://img.devrant.com/devrant/rant/r_355835_mYbbd.jpg'],
          ['White Bread\n","Amount: 100 grams","Calories: 265","Total fat (g): 3.2","Cholesterol (mg): 0","Protein (g): 9","Sodium (mg): 491", "Iron (%): 19', 'https://www.saveur.com/sites/saveur.com/files/milk-bread-14_2000x1500.jpg'],
         ]

states = ['Write your full name👇',
          'Write your age👇',
          'How many calories do you want to intake during a day?👇',
          'Write your allergies',
          'Write your diet👇',
          'Write your gender👇',
          'You are already registered👇']

def pdf(call):
    print(call.message.chat.id)
    if call.data == 'PDFyes':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="http://www.sovel.org/images/upload/ru/1565/ProgramSIP_28032019.pdf")
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Good")

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
   # keyboard.add(types.InlineKeyboardButton(text='Male', callback_data='PDFyes'))
   # keyboard.add(types.InlineKeyboardButton(text='Female', callback_data='PDFno'))
    bot.send_message(message.chat.id, "Take a photo of your meal and I will calculate how many calories in it and is it appropriate with your diet and preferences", reply_markup=keyboard)

    #if not message.chat.id in data:
      #  data[message.chat.id] = {'one': 0, 'calories': None}

  #  bot.send_message(message.chat.id, states[data[message.chat.id]['one']])

@bot.message_handler(func=lambda msg: msg.text == 'Calculate calories')
def place(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "Write your meal and how many grams of it you will have - I will automatically calculate all your calories")
    #bot.send_location(message.chat.id, '55.784587', '37.672109')

@bot.message_handler(func=lambda msg: msg.text == 'Write what you are eating')
def rules(message):
    print(message.chat.id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Vegetarian', callback_data='card'))
    keyboard.add(types.InlineKeyboardButton(text='Kosher', callback_data='card'))
    keyboard.add(types.InlineKeyboardButton(text='Halal', callback_data='card'))

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
        bot.send_message(call.message.chat.id, 'Now we will suggest you products and notice if the products that you are eating are not in your diet')
    if call.data in ['cardYes', 'cardNo']:
        file = open('data.txt', 'r')
        data = eval(file.read())
        file.close()
        print(data)

        if data[call.message.chat.id]['state'] == 5:
            data[call.message.chat.id]['money'] = call.data
            data[call.message.chat.id]['state'] += 1

            if call.data == 'cardYes':
                bot.send_message(call.message.chat.id, 'Card')
            elif call.data == 'cardNo':
                bot.send_message(call.message.chat.id, 'You are successfully registered! ')
                for a in admin:
                    bot.send_message(a, str(data[call.message.chat.id]))

            file = open('data.txt', 'w')
            file.write(str(data))
            file.close()

@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    print('check')
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Try to pay again in a few minutes, we need a small rest.")

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
    bot.send_message(message.chat.id, 'Thank you', parse_mode='Markdown')

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

                bot.send_message(message.chat.id, 'Photo was successfully uploaded.\n You will have your report shortly.')
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
