import telebot, re, random
from tok import token

bot = telebot.TeleBot(token)# токен бота

word_number = ['первый', 'второй', 'третий']

banned_words = ['dick', 'vagina', 'cunt', 'cock', 'ass', 'prostitute', 'slut', 'whore', 'fuck', 'slut', 'shit']

word_key = {'богат': 0, 'рестора': 0, 'бедн': 0, 'работ': 0, 'прививк': 0, 'covid-19': 0, 'коронавирус': 0,
            'вирус': 0, 'мяс': 1, 'растен': 1, 'коров': 1,
            'веган': 1, 'пенальт': 2, 'финал': 2, 'правда': 2, 'vip': 3, 'qr': 3, 'коды': 3, 'мероприят': 3,
            'вакцин': 3, 'пандемия': 3, 'молод': 4, 'косяк': 4,
            'ошибк': 4, 'счаст': 5, 'глухонем': 5, 'муму': 5, 'литератур': 5, 'стринг': 6, 'лгбт': 6, 'мент': 7,
            'полиция': 7, 'правосуд': 7, 'закон': 7,
            'порядок': 7, 'преступ': 7}

array_anecdotes = ['Я правильно понял, что богатые ставят прививку, что б ходить по '
                   'ресторанам, а бедные – что б ходить на работу?',#богат рестора бедн работ прививк covid-19 коронавирус вирус
                   'Проблема производства мяса из растений состоит в том, что уже существует ' 
                   'высокоэффективная технология производства мяса из растений – корова.',#мясо растен коров веган
                   'Не умеешь бить пенальти – нефиг в финал пробиваться всеми правдами и неправдами!',# пенальт финал правда
                   ' Как скоро появится VIP QR-коды позволяющие проводить на мероприятия невакцинированых особей?',# VIP QR коды мероприят вакцин пандемия
                   'С теперешним бы умом да обратно в молодость… Уж я бы накосячил гораздо интереснее',# молод косяк ошибк
                   'Может, мы были бы в целом чуть счастливее, если бы в 5м классе не читали, как одинокий '
                   'глухонемой мужчина топит единственное существо, которое его любит?',# счаст глухонем муму литератур
                   'Олег купил Оксане стринги, но ради шутки сам надел. А через месяц в этих стрингах он целовал уже Петра',# стринг лгбт
                   'Я сегодня не планировал выходить на пробежку, но менты появились так неожиданно']# мент полиция правосуд закон порядок преступ

@bot.message_handler(commands=['картинку'])
def for_command(m):

    bot.send_photo(m.chat.id, f'https://picsum.photos/id/{random.randrange(0,1084)}/1280/1024')

@bot.message_handler(content_types=['text'])
def for_anecdotes_editing(mes):

    text = mes.text.lower()
    anecdotes_for_send = []

    for ban_word in banned_words:
        if re.search(rf'{ban_word}', text):
            bot.delete_message(mes.chat.id, mes.message_id)
            bot.send_message(mes.chat.id, f'{mes.from_user.first_name} такие слова у нас запрещены. Прекрати это!')

            return

    if re.search('bot пришли мне картинку', text):
        bot.send_message(mes.chat.id, 'ОК отправь команду /картинку')
        return

    if re.search('ghbdtn', text):
        bot.send_message(mes.chat.id, f'{mes.from_user.first_name} хотел сказать привет')

    for word, value in word_key.items():
        if re.search(rf'{word}', text):
            anecdotes_for_send.append(array_anecdotes[value])

    if len(anecdotes_for_send) > 1:
        bot.send_message(mes.chat.id, 'Кажется я вспомнил сразу несколько несмешных анекдотов')

        for anecdot in enumerate(anecdotes_for_send):
            bot.send_message(mes.chat.id, f'Вот {word_number[anecdot[0]]} из них {anecdot[1]}')

    if len(anecdotes_for_send) == 1:
        bot.send_message(mes.chat.id, f'Кажется я вспомнил несмешной анекдот {anecdotes_for_send[0]}')

bot.polling()