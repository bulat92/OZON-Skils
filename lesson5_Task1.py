anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

def shows_matcher(names, dict_1, dict_2):
    dict_1 = set(dict_1.values())
    dict_2 = set(dict_2.values())

    if dict_1.intersection(dict_2):

        consilience = dict_1.intersection(dict_2)

        print(f"У {names} общие любимые жанры сериалов это", end=' ')

        for i in consilience:
            print(i, end=' ')
        print()
    else:
        print(f"У {names} нет общих любимых жанров")

shows_matcher('Ани и Насти', anya, nastya)
shows_matcher('Оли и Светы', olya, sveta)
shows_matcher('Светы и Ани', sveta, anya)