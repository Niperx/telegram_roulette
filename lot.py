# coding=utf-8
import telebot
import time
from datetime import datetime
import json
import random
import os
import os.path
from telebot import types
from threading import *
from settings import *

bot = telebot.TeleBot(token);

core_way = "/home/Niperx/"
user_way = "/home/Niperx/users/"
# core_way = "F:/TGBot/users/"


def get_logs(text):
	with open(core_way + "logs.txt", "r") as read_logs:
		logs_text = read_logs.read()

	logs_text += text + "\n"

	with open(core_way + "logs.txt", "w") as write_logs:
		write_logs.write(logs_text)


def alert(num, msg):
	time.sleep(num)
	bot.send_message(msg.chat.id, 'Я поспал 10 секунд')



@bot.message_handler(commands=['time']) # balance - Проверить свой баланс.
def alert_time(message):
	t1 = Thread(target = alert, args = (5, message,))
	t1.start()



@bot.message_handler(commands=['reg']) # reg - Зарегистрировать пользователя.
def reg_user(message):

    try:

    	file_path = user_way + str(message.from_user.id) + ".json"

    	if os.path.exists(file_path) == False:

    		user = { 'id' : message.from_user.id, 'username' : message.from_user.username, 'first_name' : message.from_user.first_name, 'balance' : 10000, 'money_time' : time.strftime("%m%d")}

    		with open(file_path, 'w', encoding='utf-8') as write_user:
    			json.dump(user, write_user, ensure_ascii=False, indent=4)

    		now = datetime.now()
    		now = datetime.strftime(now, '%d.%m %H:%M:%S')
    		print(now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") зарегистрировался в игре!")

    		bot.send_message(message.chat.id, "@" + message.from_user.username + ", Добро пожаловать в таблицу игроков!")

    	elif os.path.exists(file_path) == True:

    		bot.send_message(message.chat.id, "@" + message.from_user.username + ", Вы уже зарегистрированы!")

    except:
        bot.send_message(message.chat.id, message.from_user.first_name + ", У вас отсутствует никнейм или имя в информации аккаунта!\nНастройте свой аккаунт.")

@bot.message_handler(commands=['start']) # start - Зарегистрировать пользователя.
def start_user(message):

    bot.send_message(message.chat.id, 'Добро пожаловать в это 🎰 Чёртово Казино 🎰, команды вы можете посмотреть написав "/help"')



@bot.message_handler(commands=['black'])
def bet_black(message):
	keyboard = types.InlineKeyboardMarkup()
	callback_button = types.InlineKeyboardButton(text="100", callback_data="100b")
	callback_button2 = types.InlineKeyboardButton(text="200", callback_data="200b")
	callback_button3 = types.InlineKeyboardButton(text="400", callback_data="400b")
	callback_button4 = types.InlineKeyboardButton(text="800", callback_data="800b")
	callback_button5 = types.InlineKeyboardButton(text="1600", callback_data="1600b")
	callback_button6 = types.InlineKeyboardButton(text="All in", callback_data="allb")
	keyboard.add(callback_button, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
	bot.send_message(message.chat.id, "Выберите вашу ставку", reply_markup=keyboard)

	msg_info = {"chat_id" : message.chat.id, "user_id" : message.from_user.id, "first_name" : message.from_user.first_name, "username" : message.from_user.username}
	with open(core_way + "message" + str(message.from_user.id) +".json", 'w', encoding='utf-8') as write_message:
		json.dump(msg_info, write_message, ensure_ascii=False, indent=4)

@bot.message_handler(commands=['red'])
def bet_red(message):
	keyboard = types.InlineKeyboardMarkup()
	callback_button = types.InlineKeyboardButton(text="100", callback_data="100r")
	callback_button2 = types.InlineKeyboardButton(text="200", callback_data="200r")
	callback_button3 = types.InlineKeyboardButton(text="400", callback_data="400r")
	callback_button4 = types.InlineKeyboardButton(text="800", callback_data="800r")
	callback_button5 = types.InlineKeyboardButton(text="1600", callback_data="1600r")
	callback_button6 = types.InlineKeyboardButton(text="All in", callback_data="allr")
	keyboard.add(callback_button, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
	bot.send_message(message.chat.id, "Выберите вашу ставку", reply_markup=keyboard)

	msg_info = {"chat_id" : message.chat.id, "user_id" : message.from_user.id, "first_name" : message.from_user.first_name, "username" : message.from_user.username}
	with open(core_way + "message" + str(message.from_user.id) +".json", 'w', encoding='utf-8') as write_message:
		json.dump(msg_info, write_message, ensure_ascii=False, indent=4)

@bot.message_handler(commands=['green'])
def bet_green(message):
	keyboard = types.InlineKeyboardMarkup()
	callback_button = types.InlineKeyboardButton(text="100", callback_data="100g")
	callback_button2 = types.InlineKeyboardButton(text="200", callback_data="200g")
	callback_button3 = types.InlineKeyboardButton(text="400", callback_data="400g")
	callback_button4 = types.InlineKeyboardButton(text="800", callback_data="800g")
	callback_button5 = types.InlineKeyboardButton(text="1600", callback_data="1600g")
	callback_button6 = types.InlineKeyboardButton(text="All in", callback_data="allg")
	keyboard.add(callback_button, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
	bot.send_message(message.chat.id, "Выберите вашу ставку", reply_markup=keyboard)

	msg_info = {"chat_id" : message.chat.id, "user_id" : message.from_user.id, "first_name" : message.from_user.first_name, "username" : message.from_user.username}
	with open(core_way + "message" + str(message.from_user.id) +".json", 'w', encoding='utf-8') as write_message:
		json.dump(msg_info, write_message, ensure_ascii=False, indent=4)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    try:

        with open(core_way + "message" + str(call.from_user.id) +".json", 'r', encoding='utf-8') as read_message:
            message = json.load(read_message)

        if call.from_user.id == message["user_id"]:

            if call.message:
                if call.data == "100b" or call.data == "200b" or call.data == "400b" or call.data == "800b" or call.data == "1600b" or call.data == "allb":

                    file_path = user_way + str(message["user_id"]) + ".json"

                    if os.path.exists(file_path) == True:

                        with open(file_path, 'r', encoding='utf-8') as read_user:
                            user = json.load(read_user)

                        if call.data == "allb":
                            summ = user['balance']
                        else:
                            summ = int(call.data[:len(call.data)-1])

                        if user['balance'] >= summ and user['balance'] != 0:

                            roll = random.randint(0, 14)
                            roll_pic = "✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                            with open(core_way + "stat.json", 'r', encoding='utf-8') as read_stat:
                                stat = json.load(read_stat)

                            stat[str(roll)] += 1
                            stat["100"] += 1

                            with open(core_way + "stat.json", 'w', encoding='utf-8') as write_stat:
                                json.dump(stat, write_stat, ensure_ascii=False, indent=4)

                            if roll != 6:
                                if roll % 2 == 0:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] += summ

                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Чёрное. Выпало Чёрное(" + str(roll) + "). Выиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n⬛️ Чёрное ⬛️\n\n" + message["first_name"] + ", Вы выиграли " + str(summ) + " 💰 шекелей!")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                                elif roll % 2 == 1:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] -= summ
                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Чёрное. Выпало Красное(" + str(roll) + "). Проиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟥 Красное 🟥\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                            elif roll == 6:

                                roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                roll_pic = "✖️✖️✖️✖️✖️✖️🎲✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                                user['balance'] -= summ

                                now = datetime.now()
                                now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Чёрное. Выпало Зелёное(" + str(roll) + "). Проиграл: " + str(summ)
                                print(text)
                                get_logs(text)

                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟩 Зелёное 🟩\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                with open(file_path, 'w', encoding='utf-8') as write_user:
                                    json.dump(user, write_user, ensure_ascii=False, indent=4)

                        elif user['balance'] < summ:

                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "У вас недостаточно средств.")

                    elif os.path.exists(file_path) == False:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "@" + message["username"] + ", Вы не зарегистрированы!")


                if call.data == "100r" or call.data == "200r" or call.data == "400r" or call.data == "800r" or call.data == "1600r" or call.data == "allr":

                    file_path = user_way + str(message["user_id"]) + ".json"

                    if os.path.exists(file_path) == True:

                        with open(file_path, 'r', encoding='utf-8') as read_user:
                            user = json.load(read_user)

                        if call.data != "allr":
                            summ = int(call.data[:len(call.data)-1])
                        else:
                            summ = user['balance']

                        if user['balance'] >= summ and user['balance'] != 0:

                            roll = random.randint(0, 14)
                            roll_pic = "✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                            with open(core_way + "stat.json", 'r', encoding='utf-8') as read_stat:
                                stat = json.load(read_stat)

                            stat[str(roll)] += 1
                            stat["100"] += 1

                            with open(core_way + "stat.json", 'w', encoding='utf-8') as write_stat:
                                json.dump(stat, write_stat, ensure_ascii=False, indent=4)

                            if roll != 6:
                                if roll % 2 == 0:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] -= summ

                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Красное. Выпало Чёрное(" + str(roll) + "). Проиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n⬛️ Чёрное ⬛️\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                                elif roll % 2 == 1:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] += summ

                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Красное. Выпало Красное(" + str(roll) + "). Выиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟥 Красное 🟥\n\n" + message["first_name"] + ", Вы выиграли " + str(summ) + " 💰 шекелей!")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                            elif roll == 6:

                                roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                roll_pic = "✖️✖️✖️✖️✖️✖️🎲✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                                user['balance'] -= summ

                                now = datetime.now()
                                now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Красное. Выпало Зелёное(" + str(roll) + "). Проиграл: " + str(summ)
                                print(text)
                                get_logs(text)

                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟩 Зелёное 🟩\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                with open(file_path, 'w', encoding='utf-8') as write_user:
                                    json.dump(user, write_user, ensure_ascii=False, indent=4)

                        elif user['balance'] < summ:

                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "У вас недостаточно средств.")

                    elif os.path.exists(file_path) == False:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "@" + message["username"] + ", Вы не зарегистрированы!")

                if call.data == "100g" or call.data == "200g" or call.data == "400g" or call.data == "800g" or call.data == "1600g" or call.data == "allg":

                    file_path = user_way + str(message["user_id"]) + ".json"

                    if os.path.exists(file_path) == True:

                        with open(file_path, 'r', encoding='utf-8') as read_user:
                            user = json.load(read_user)

                        if call.data != "allg":
                            summ = int(call.data[:len(call.data)-1])
                        else:
                            summ = user['balance']

                        if user['balance'] >= summ:

                            roll = random.randint(0, 14)
                            roll_pic = "✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                            with open(core_way + "stat.json", 'r', encoding='utf-8') as read_stat:
                                stat = json.load(read_stat)

                            stat[str(roll)] += 1
                            stat["100"] += 1

                            with open(core_way + "stat.json", 'w', encoding='utf-8') as write_stat:
                                json.dump(stat, write_stat, ensure_ascii=False, indent=4)

                            if roll != 6:
                                if roll % 2 == 0:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] -= summ

                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Зелёное. Выпало Чёрное(" + str(roll) + "). Проиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n⬛️ Чёрное ⬛️\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                                elif roll % 2 == 1:

                                    roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                    roll_pic = roll_pic[:roll*2] + '🎲' + roll_pic[roll*2+1:]

                                    user['balance'] -= summ

                                    now = datetime.now()
                                    now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                    text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Зелёное. Выпало Красное(" + str(roll) + "). Проиграл: " + str(summ)
                                    print(text)
                                    get_logs(text)

                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟥 Красное 🟥\n\n" + message["first_name"] + ", Вы проиграли " + str(summ) + " 💰 шекелей... :(")

                                    with open(file_path, 'w', encoding='utf-8') as write_user:
                                        json.dump(user, write_user, ensure_ascii=False, indent=4)

                            elif roll == 6:

                                roll_start = "🎰 Крутим рулетку 🎰\n\n"
                                roll_pic = "✖️✖️✖️✖️✖️✖️🎲✖️✖️✖️✖️✖️✖️✖️✖️\n⬛️🟥⬛️🟥⬛️🟥🟩🟥⬛️🟥⬛️🟥⬛️🟥⬛️\n"

                                user['balance'] += summ*13

                                now = datetime.now()
                                now = datetime.strftime(now, '%d.%m %H:%M:%S')
                                text = now + "  @" + user['username'] + " (" + user['first_name'] + ") крутанул рулетку поставив на Зелёное. Выпало Зелёное(" + str(roll) + "). Выиграл: " + str(summ*13)
                                print(text)
                                get_logs(text)

                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = roll_start + roll_pic + "\nНа барабане следующий цвет:\n🟩 Зелёное 🟩\n\n" + message["first_name"] + ", Вы выиграли " + str(summ*13) + " 💰 шекелей!")

                                with open(file_path, 'w', encoding='utf-8') as write_user:
                                    json.dump(user, write_user, ensure_ascii=False, indent=4)

                        elif user['balance'] < summ:

                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "У вас недостаточно средств.")

                    elif os.path.exists(file_path) == False:

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "@" + message["username"] + ", Вы не зарегистрированы!")

            os.remove(core_way + "message" + str(call.from_user.id) +".json")

        else:
            bot.send_message(call.from_user.id, call.from_user.first_name + ", Это не ваша ставка!")

    except :

        bot.send_message(call.from_user.id, call.from_user.first_name + ", у вас нет ставки.")















@bot.message_handler(commands=['balance']) # balance - Проверить свой баланс.
def check_balance(message):
	file_path = user_way + str(message.from_user.id) + ".json"

	if os.path.exists(file_path) == True:

		with open(file_path, 'r', encoding='utf-8') as read_user:
			user = json.load(read_user)

		bot.send_message(message.chat.id, "@" + message.from_user.username + ", Ваш баланс: " + str(user['balance']) + "💰")

		now = datetime.now()
		now = datetime.strftime(now, '%d.%m %H:%M:%S')
		text = now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") посмотрел свой баланс (" + str(user['balance']) + " шекелей)"
		print(text)
		print(message.chat.id)
		get_logs(text)

	elif os.path.exists(file_path) == False:

		bot.send_message(message.chat.id, "@" + message.from_user.username + ", Вы не зарегистрированы!")
		print(message.chat.id)


@bot.message_handler(commands=['stats']) # stats - Проверить статистику рандома.
def check_stats(message):

    with open("/home/Niperx/stat.json", 'r', encoding='utf-8') as read_stat: # �🟥⬛
        stat = json.load(read_stat)

    stat_text = "Статистика рандома:\n\n"
    stat_red = 0
    stat_black = 0
    stat_green = 0

    for key in stat:
        if key != "100":
            if int(key) != 6:
                if int(key) % 2 == 1:
                    stat_red += stat[key]
                elif int(key) % 2 == 0:
                    stat_black += stat[key]
            elif int(key) == 6:
                stat_green += stat[key]



    stat_text += "🟥 Красный цвет выпал " + str(stat_red) + " раз(а) 🟥 (" + str(round(stat_red/(stat["100"]/100))) + "%)\n\n"
    stat_text += "⬛️ Чёрный цвет выпал " + str(stat_black) + " раз(а) ⬛️ (" + str(round(stat_black/(stat["100"]/100))) + "%)\n\n"
    stat_text += "🟩 Зелёный цвет выпал " + str(stat_green) + " раз(а) 🟩 (" + str(round(stat_green/(stat["100"]/100))) + "%)\n\n"

    stat_text += "\nОбщее число бросков - " + str(stat["100"]) + " раз"

    now = datetime.now()
    now = datetime.strftime(now, '%d.%m %H:%M:%S')
    text = now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") посмотрел статистику рандома"
    print(text)
    get_logs(text)

    bot.send_message(message.chat.id, stat_text)

@bot.message_handler(commands=['leaders']) # leads - Показать список лидеров.
def check_leaders(message):

    file_path = user_way + str(message.from_user.id) + ".json"

    user_tab = os.listdir(user_way)

    lead_tab = {}

    for i in user_tab:
        file_path = user_way + i

        with open(file_path, 'r', encoding='utf-8') as read_user:
            user = json.load(read_user)

        lead_tab.update({user['username'] : user['balance']})

    lead_text = "⭐️ ТОП-10 богатейших людей этого чёртово казино! ⭐️️ \n\n"

    y = 1
    k = {k: v for k, v in sorted(lead_tab.items(), key=lambda item: item[1], reverse=True)}
    for key in k:
        if y == 1:
            smile = "🥇"
        elif y == 2:
            smile = "🥈"
        elif y == 3:
            smile = "🥉"
        else:
            smile = "🎗"
        you_mark = ""
        if message.from_user.username == key:
            you_mark = "(Вы)"
        lead_text += smile + " " + str(y) + ". " + key + " - " + str(k[key]) + " шекелей. " + smile + " " + you_mark + "\n"
        if y == 10:
            break
        y += 1

    now = datetime.now()
    now = datetime.strftime(now, '%d.%m %H:%M:%S')
    text = now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") посмотрел список лидеров"
    print(text)
    get_logs(text)


    bot.send_message(message.chat.id, lead_text)

@bot.message_handler(commands=['help']) # help - Показать список комманд.
def check_commands(message):
	text = "/black - Поставить шекели на чёрное.\n"
	text += "/red - Поставить шекели на красное.\n"
	text += "/green - Поставить шекели на зелёное.\n"
	text += "/balance - Проверить свой баланс.\n"
	text += "/money - Получить ежедневную норму баблишка.\n"
	text += "/leaders - Показать список лидеров.\n"
	text += "/stats - Проверить статистику рандома.\n"
	text += "/reg - Зарегистрироваться.\n"
	text += "/help - Показать список команд."
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['money']) # start - Запуск бота в группе (Только для разработчиков).
def get_money(message):

	file_path = user_way + str(message.from_user.id) + ".json"

	if os.path.exists(file_path) == True:

		with open(file_path, 'r', encoding='utf-8') as read_user:
			user = json.load(read_user)

		money_time = user['money_time']
		if money_time[:2] != time.strftime("%m"):
			money_time = time.strftime("%m") + "00"

		if money_time < time.strftime("%m%d"):
			user['balance'] += 100000
			user['money_time'] = time.strftime("%m%d")

			now = datetime.now()
			now = datetime.strftime(now, '%d.%m %H:%M:%S')
			text = now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") получил(а) ежедневную норму в 100000 шекелей"
			print(text)
			get_logs(text)

			bot.send_message(message.chat.id, message.from_user.first_name + ", Вам начислено 100000 шекелей на счёт!")

			with open(file_path, 'w', encoding='utf-8') as write_user:
				json.dump(user, write_user, ensure_ascii=False, indent=4)

		elif money_time == time.strftime("%m%d"):
			bot.send_message(message.chat.id, message.from_user.first_name + ", Вы уже получили на сегодня свою норму баблишка. Имейте совесть...")

			now = datetime.now()
			now = datetime.strftime(now, '%d.%m %H:%M:%S')
			text = now + "  @" + message.from_user.username + " (" + message.from_user.first_name + ") попытался получить ежедевные деньги ещё раз"
			print(text)
			get_logs(text)

	elif os.path.exists(file_path) == False:

		bot.send_message(message.chat.id, "@" + message.from_user.username + ", Вы не зарегистрированы!")


bot.polling(none_stop=True, interval=0)