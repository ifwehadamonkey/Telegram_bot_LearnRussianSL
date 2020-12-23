import telebot
from telebot import types

bot = telebot.TeleBot("786106722:AAGIQZSe-0owTMuvwBaGjUsOc7E2GROIW58")

commands = {
    'start': 'Начало работы с ботом',
    'help': 'Информация по командам бота',
    'links': 'Допольнительные источники для изучения',
    'dictionary': 'Узнай больше слов на языке жестов'
}

alphabet = {
    'а': 'https://abvgdee.ru/images/alfavit/gluhonemyh/a.png',
    'б': 'https://abvgdee.ru/images/alfavit/gluhonemyh/b.png',
    'в': 'https://abvgdee.ru/images/alfavit/gluhonemyh/v.png',
    'г': 'https://abvgdee.ru/images/alfavit/gluhonemyh/g.png',
    'д': 'https://abvgdee.ru/images/alfavit/gluhonemyh/d.png',
    'е': 'https://abvgdee.ru/images/alfavit/gluhonemyh/e.png',
    'ж': 'https://abvgdee.ru/images/alfavit/gluhonemyh/zh.png',
    'з': 'https://abvgdee.ru/images/alfavit/gluhonemyh/z.png',
    'и': 'https://abvgdee.ru/images/alfavit/gluhonemyh/i.png',
    'й': 'https://abvgdee.ru/images/alfavit/gluhonemyh/j.png',
    'к': 'https://abvgdee.ru/images/alfavit/gluhonemyh/k.png',
    'л': 'https://abvgdee.ru/images/alfavit/gluhonemyh/l.png',
    'м': 'https://abvgdee.ru/images/alfavit/gluhonemyh/m.png',
    'н': 'https://abvgdee.ru/images/alfavit/gluhonemyh/n.png',
    'о': 'https://abvgdee.ru/images/alfavit/gluhonemyh/o.png',
    'п': 'https://abvgdee.ru/images/alfavit/gluhonemyh/p.png',
    'р': 'https://abvgdee.ru/images/alfavit/gluhonemyh/r.png',
    'с': 'https://abvgdee.ru/images/alfavit/gluhonemyh/s.png',
    'т': 'https://abvgdee.ru/images/alfavit/gluhonemyh/t.png',
    'у': 'https://abvgdee.ru/images/alfavit/gluhonemyh/u.png',
    'ф': 'https://abvgdee.ru/images/alfavit/gluhonemyh/f.png',
    'х': 'https://abvgdee.ru/images/alfavit/gluhonemyh/h.png',
    'ц': 'https://abvgdee.ru/images/alfavit/gluhonemyh/ts.png',
    'ч': 'https://abvgdee.ru/images/alfavit/gluhonemyh/ch.png',
    'ш': 'https://abvgdee.ru/images/alfavit/gluhonemyh/sh.png',
    'щ': 'https://abvgdee.ru/images/alfavit/gluhonemyh/shch.png',
    'ъ': 'https://abvgdee.ru/images/alfavit/gluhonemyh/tvjordyj-znak.png',
    'ы': 'https://abvgdee.ru/images/alfavit/gluhonemyh/y.png',
    'ь': 'https://abvgdee.ru/images/alfavit/gluhonemyh/myagkij-znak.png',
    'э': 'https://abvgdee.ru/images/alfavit/gluhonemyh/ee.png',
    'ю': 'https://abvgdee.ru/images/alfavit/gluhonemyh/yu.png',
    'я': 'https://abvgdee.ru/images/alfavit/gluhonemyh/ya.png',
}

emotions = {'апатия': 'https://media.spreadthesign.com/video/mp4/12/26950.mp4',
            'боль': 'https://media.spreadthesign.com/video/mp4/12/4439.mp4',
            'безразличие': 'https://media.spreadthesign.com/video/mp4/12/296729.mp4',
            'благодарный': 'https://media.spreadthesign.com/video/mp4/12/43658.mp4',
            'возрадоваться': 'https://media.spreadthesign.com/video/mp4/12/296382.mp4',
            'веселый': 'https://media.spreadthesign.com/video/mp4/12/176715.mp4',
            'влюбленный': 'https://media.spreadthesign.com/video/mp4/12/295228.mp4',
            }

hello = {'добро пожаловать': 'https://media.spreadthesign.com/video/mp4/12/18420.mp4',
         'пока': 'https://media.spreadthesign.com/video/mp4/12/100036.mp4',
         'привет': 'https://media.spreadthesign.com/video/mp4/12/17658.mp4',
         'с днем рождения': 'https://media.spreadthesign.com/video/mp4/12/295884.mp4',
         'позвонить на сервис': 'https://media.spreadthesign.com/video/mp4/12/134844.mp4',
         }

idioms = {'слава богу': 'https://media.spreadthesign.com/video/mp4/12/321197.mp4',
          'счастливого пути': 'https://media.spreadthesign.com/video/mp4/12/227221.mp4',
          'держать себя в руках': 'https://media.spreadthesign.com/video/mp4/12/133763.mp4',
          'будет сделано': 'https://media.spreadthesign.com/video/mp4/12/18542.mp4',
          'легок на помине': 'https://media.spreadthesign.com/video/mp4/12/315696.mp4'
          }

colors = {'красный': 'https://media.spreadthesign.com/video/mp4/12/4495.mp4',
          'желтый': 'https://media.spreadthesign.com/video/mp4/12/5776.mp4',
          'зеленый': 'https://media.spreadthesign.com/video/mp4/12/5717.mp4',
          'темнота': 'https://media.spreadthesign.com/video/mp4/12/349236.mp4',
          'белый': 'https://media.spreadthesign.com/video/mp4/12/4425.mp4'
          }


@bot.message_handler(commands=["dictionary"])
def inline(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton('Эмоции', callback_data='эмоции'),
        types.InlineKeyboardButton('Фразы', callback_data='фразы'),
        types.InlineKeyboardButton('Идиомы', callback_data='идиомы'),
        types.InlineKeyboardButton('Цвета', callback_data='цвета')
    )
    bot.send_message(message.chat.id,
                     'Привет, ты можешь узнать больше слов. Выбери категорию!',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def revise(call):
    if call.data == "эмоции":
        key = ", ".join(list(emotions.keys()))
        bot.send_message(call.message.chat.id, key)
        bot.send_message(call.message.chat.id, "Напиши слово из выбранного списка!")
    elif call.data == "фразы":
        key = ", ".join(list(hello.keys()))
        bot.send_message(call.message.chat.id, key)
        bot.send_message(call.message.chat.id, "Напиши слово из выбранного списка!")
    elif call.data == "идиомы":
        key = ", ".join(list(idioms.keys()))
        bot.send_message(call.message.chat.id, key)
        bot.send_message(call.message.chat.id, "Напиши слово из выбранного списка!")
    elif call.data == "цвета":
        key = ", ".join(list(colors.keys()))
        bot.send_message(call.message.chat.id, key)
        bot.send_message(call.message.chat.id, "Напиши слово из выбранного списка!")


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Доступные команды бота: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет, попробуем выучить русский язык жестов и дактиль. Введи любую букву. ' + '\n' + 'Напиши  '
                                                                                                              '/help  '
                                                                                                              'для '
                                                                                                              'большей '
                                                                                                              'информации '
                     )


@bot.message_handler(commands=["links"])
def send_link(message):
    bot.send_message(message.chat.id, 'https://www.memrise.com/course/1379220/russkii-zhestovyi-iazyk/')
    bot.send_message(message.chat.id, 'https://jestov.net')


@bot.message_handler(content_types=['text'])
def send_words(message):
    for key in emotions:
        if message.text.lower() == key:
            bot.send_video(message.chat.id, emotions[key])
    for key in alphabet:
        if message.text.lower() == key:
            bot.send_photo(message.chat.id, alphabet[key])
    for key in hello:
        if message.text.lower() == key:
            bot.send_video(message.chat.id, hello[key])
    for key in idioms:
        if message.text.lower() == key:
            bot.send_video(message.chat.id, idioms[key])
    for key in colors:
        if message.text.lower() == key:
            bot.send_video(message.chat.id, colors[key])


bot.polling(none_stop=True, interval=0)



