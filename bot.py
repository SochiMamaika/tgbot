import telebot
bot  = telebot.TeleBot("") #просто тайтл бота

@bot.message_handler(commands=['start'])#то происходит при нажатии старт
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")#send_message это метод отправить смс
    bot.send_message(message.chat.id,"<b>Чтобы воспользоваться мной тебе нужно открыть меню</b>", parse_mode="html")

@bot.message_handler(commands=['command1'])
def command1(message):
    bot.send_message(message.chat.id,"https://sochimamaika.github.io/Sait.github.io/Cloth.html", parse_mode='html')

@bot.message_handler(commands=['command2'])
def command2(message):
    photo1=open("3.jpg",'rb')
    photo2=open("4.jpg",'rb')
    photo3=open("5.jpg",'rb')
    photo4=open("6.jpg",'rb')
    photo5=open("9.jpg",'rb')
    photo6=open("10.jpg",'rb')
    photo7=open("11.jpg",'rb')
    photo8=open("12.jpg",'rb')
    bot.send_photo(message.chat.id,photo1)#указал что именно выдаем фото
    bot.send_photo(message.chat.id,photo2)
    bot.send_photo(message.chat.id,photo3)
    bot.send_photo(message.chat.id,photo4)
    bot.send_photo(message.chat.id,photo5)
    bot.send_photo(message.chat.id,photo6)
    bot.send_photo(message.chat.id,photo7)
    bot.send_photo(message.chat.id,photo8)

@bot.message_handler(commands=['command3'])
def command3(message):
    bot.send_message(message.chat.id,"<b>Средняя цена в нашем магазине 2000 рублей!</b>", parse_mode='html')

@bot.message_handler()
def get_text(message):#Функции здесь как методы в классах
    if message.text == "привет":
        bot.send_message(message.chat.id, "И тебе привет!!!", parse_mode="html") #parse_mode что работает как в html
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет!!!", parse_mode="html")
    elif message.text == "ПРИВЕТ":
        bot.send_message(message.chat.id, "И тебе привет!!!", parse_mode="html")
    elif message.text == "ghbdtn":
        bot.send_message(message.chat.id, "И тебе привет!!! Но поменяй язык на клавиатуре)", parse_mode="html")
    elif message.text == "Ghbdtn":
        bot.send_message(message.chat.id, "И тебе привет!!! Но поменяй язык на клавиатуре)", parse_mode="html")
    elif message.text == "GHBDTN":
        bot.send_message(message.chat.id, "И тебе привет!!! Но поменяй язык на клавиатуре)", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Извините я вас не понимаю(((", parse_mode='html')

bot.polling(none_stop=True)  
