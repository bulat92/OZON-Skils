import copy

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика',
         'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

p = lambda x: print(x)

shows = {k: v for k,v in shows.items() if v == 'фантастика' or v == 'фэнтази'}#dict comprehension

p('dict comprehension')

for k, v in shows.items():
    p(f'{k},{v}')

shows = [k for k in shows]#list comprehension

p('list comprehension')
for i in shows:
    p(f'{i}')