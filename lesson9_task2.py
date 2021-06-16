import re
from printer import printer as p

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

for v in readed_file_in_list:

    result = re.search(r'Андромед', f"{v}")

    if result and v[3]:
        p(v)
        #p((re.sub(r'\'|\,|\[|\]', ' ', f"{v}")).strip())

print('======'*30+'\n')