def genre_count(dict, genre):

    number_of_shows = 0

    for v in dict.values():

        number_of_shows += 1 if genre == v else 0

    return number_of_shows

def middle_rating(dict, list):

    number_of_shows = 0
    total_value_rating = 0

    for i in list:

        if dict.get(i):
            number_of_shows += 1
            total_value_rating += dict.get(i)

    return round(total_value_rating/number_of_shows, 2)