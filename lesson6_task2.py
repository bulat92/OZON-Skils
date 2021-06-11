import pickle
shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
        'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98}, 'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма',
        'Rating': 0.82}, 'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}

def get_genre(dict): # создает список жанров

    genre_set = set() # здесь будут сохранятся жанры

    for v in dict.values(): # перечисляет значения сериалов
        for genre_in_v in v.values():#
            genre_set.add(genre_in_v)# после получения первого значения (всегда это жанр)
            break# срабатывает бреак

    return genre_set



def middle_rating_count(dict, genre):

    middle_total_rating = 0 # рейтинг у жанра в общем
    number_of_shows = 0 # число сериалов
    genre_dict = {}# словарь с сериалами и жанром

    for k in dict:

        try:
            if dict[k]['Жанр'] == genre:# если есть что то в рейтинге то
                middle_total_rating += float(dict[k]['Рейтинг']) # складывает все подходящие рейтинги
                number_of_shows += 1 #считает сколько сериалов нашлось
                genre_dict.update({k: dict[k]['Жанр']}) # сохраняет название сериала и их его жанр

        except KeyError:

            if dict[k]['Genre'] == genre:
                middle_total_rating += float(dict[k]['Rating'])
                number_of_shows += 1
                genre_dict.update({k: dict[k]['Genre']})

    file = open(f"{genre}.dat", 'wb') # запись в .дат файлы
    pickle.dump(genre_dict, file)
    file.close()

    print(f"В жанре {genre} средний рейтинг {round(middle_total_rating / number_of_shows, 2)} всего {number_of_shows} сериала!")


if __name__ == "__main__":
    for i in get_genre(shows):
        middle_rating_count(shows, i)




