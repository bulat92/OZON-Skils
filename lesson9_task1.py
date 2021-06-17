import re

readed_file = [] # конечная таблица
all_column_leng = [67, 26, 31, 94]# ширины колонок которые вычтены отдельно по самому длинному значению

with open('lesson09_closest_galaxies.txt', encoding='utf-8') as file:

    for line in file.read().split('\n'):# читаем делим на строки

        list_transient = []# сюда во временный массив будет сохраняться строка
        column_number = 0# номер колонки для смены ширины колонки в массиве all_column_leng

        for value in line.split(','):# еще делим на отдельные слова

            value = f"{value}{' '*(all_column_leng[column_number] - len(value))}"# добавляем пространство к после значения чтоб колонки были ровные
            list_transient.append(value)# заносим в строку

            column_number += 1# переходим на следующую колонку

        readed_file.append(list_transient)# заносим строку в таблицу

print('\nВ названии встречаются созвездия Рыбы, Пегас или Кит\n')

for v in readed_file:

    if re.search(r'Рыбы|Пегас|Кит', f"{v[0]}"):# находим значения что нам нужны
        print((re.sub(r'\'|\,', ' ', f"{v}")))# удаляем лишние символы печатаем

print('======'*30+'\n')
print('Название начинается с латинской буквы\n')

for v in readed_file:

    if re.match(r'[A-Za-z]', f"{v[0]}"):
        print((re.sub(r'\'|\,', ' ', f"{v}")))

print('======'*30+'\n')
print('Название заканчивается цифрой\n')

for v in readed_file:

    if re.search(r'[0-9]', f"{v[0]}"):
        print((re.sub(r'\'|\,', ' ', f"{v}")))