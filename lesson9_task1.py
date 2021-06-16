import re

readed_file = []
readed_file_in_list = []

with open('lesson09_closest_galaxies.txt', encoding='utf-8') as file:
    for v in file.read().split('\n'):
        readed_file.append(v)

all_column_leng = [67, 26, 31, 94]

for line in readed_file:

    list_transient = []
    column_number = 0

    for value in line.split(','):


        value = f"{value}  {' '*(all_column_leng[column_number] - len(value))}"
        list_transient.append(value)

        column_number += 1

    readed_file_in_list.append(list_transient)

print('\nВ названии встречаются созвездия Рыбы, Пегас или Кит\n')

for v in readed_file_in_list:

    if re.search(r'Рыбы|Пегас|Кит', f"{v[0]}"):
        print((re.sub(r'\'|\,|\[|\]', ' ', f"{v}")).strip())

print('======'*30+'\n')
print('Название начинается с латинской буквы\n')

for v in readed_file_in_list:

    if re.match(r'[A-Za-z]', f"{v[0]}"):
        print((re.sub(r'\'|\,|\[|\]', ' ', f"{v}")).strip())

print('======'*30+'\n')
print('Название заканчивается цифрой\n')

for v in readed_file_in_list:

    if re.search(r'[0-9]', f"{v[0]}"):
        print((re.sub(r'\'|\,|\[|\]', ' ', f"{v}")).strip())