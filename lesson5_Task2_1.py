def genre_count(dict, genre):# получает словарь и жанр

    number_of_shows = 0 # число совпадений

    for v in dict.values():# проверка по списку

        number_of_shows += 1 if genre == v else 0 # если есть совпадение то значение увеличивается на 1

    return number_of_shows

def middle_rating(dict, list):# получает словарь и список

    number_of_shows = 0 #число совпадений
    total_value_rating = 0 #общее число рейтингов

    for i in list:

        if dict.get(i): # если фильм из списка есть в словаре то
            number_of_shows += 1
            total_value_rating += dict.get(i) # сложение все рейтингов

    return round(total_value_rating/number_of_shows, 2)