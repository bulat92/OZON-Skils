shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
        'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98}, 'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма',
        'Rating': 0.82}, 'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}

def middle_rating_count(dict):

    middle_total_rating = 0# рейтинг у жанра в общем
    number_of_shows = 0# число сериалов

    for k in dict:

        try:
            if dict[k]['Рейтинг']: # если есть что то в рейтинге то
                middle_total_rating += float(dict[k]['Рейтинг'])# складывает все подходящие рейтинги
                number_of_shows += 1 #считает сколько сериалов нашлось

        except KeyError:

            if dict[k]['Rating']:
                middle_total_rating += float(dict[k]['Rating'])
                number_of_shows += 1

    return round(middle_total_rating / number_of_shows, 2)


if __name__ == "__main__":
    print(middle_rating_count(shows))