import re

andromeda_list = [] # конечная таблица
all_column_leng = [58, 14, 0, 0]# ширины колонок которые вычтены отдельно по самому длинному значению

with open('lesson09_closest_galaxies.txt', encoding='utf-8') as file:

    for line in file.read().split('\n'):# читаем делим на строки

        list_transient = []# сюда во временный массив будет сохраняться строка
        column_number = 0# номер колонки для смены ширины колонки в массиве all_column_leng

        if re.search(r'Андромед', f"{line}") and line[3]:
        # если слово Андромеда есть в строке и у нее есть растояние от земли
            for value in line.split(','):# еще делим на отдельные слова

                if column_number == 2: # в третьей колонке расстояние до земли
                    value = round(float(re.sub(r'\[[0-9]+\]|\?', ' ', f"{value}")), 1)
                    # туть происходит много чего (округление,перевод в дробь из строки, филтрация скобок и тд)
                value = f"{value}  {' '*(all_column_leng[column_number] - len(str(value)))}"
                # добавляем пространство к после значения чтоб колонки были ровные   value переводим в строку чтоб узнать длинну
                list_transient.append(value)

                column_number += 1# переходим на следующую колонку

            andromeda_list.append(list_transient)# заносим строку в таблицу

andromeda_list[0], andromeda_list[len(andromeda_list)-1] = andromeda_list[len(andromeda_list)-1], andromeda_list[0]
# таблица изначально была отсортирована по 3 клонке. Спутаем первое и последнее значение
andromeda_list.sort(key = lambda x: x[2])
#сортировака по 3 клонке

for v in andromeda_list:

    print(re.sub(r'\'|\,', ' ', f"{v}"))

