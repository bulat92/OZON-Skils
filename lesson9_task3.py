import re
from printer import printer as p

cat_value = 0

with open('lesson09_cats_of_ulthar.txt', encoding='ANSI') as file:
    for v in file.read().split():

        if re.search(r'кот', v) or re.search(r'кош', v):

            cat_value += 1

print(cat_value)