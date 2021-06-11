anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

def shows_matcher(dict_1, dict_2, names = 'хз кого'):# принимается 3 параметра
    dict_1 = set(dict_1.values())# перевод значений из словаря во множество потому что у него есть нужный метод intersection
    dict_2 = set(dict_2.values())# перевод значений из словаря во множество потому что у него есть нужный метод intersection

    if dict_1.intersection(dict_2): # если совпадения есть

        consilience = dict_1.intersection(dict_2)# запись списка совпадений

        print(f"У {names} общие любимые жанры сериалов это", end=' ')

        for i in consilience:# печать списка совпадений
            print(i, end=' ')
        print()
    else:# если нет совпадений
        print(f"У {names} нет общих любимых жанров")

shows_matcher(anya, nastya, 'Ани и Насти',)
shows_matcher(olya, sveta, 'Оли и Светы',)
shows_matcher(sveta, anya, 'Светы и Ани',)