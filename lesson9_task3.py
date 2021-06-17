import re

cat_value = 0

with open('lesson09_cats_of_ulthar.txt', encoding='ANSI') as file: # открыли файл
    for v in file.read().split():# поделили все на слова

        if (re.search(r'кот', v.lower()) or re.search(r'кош', v.lower())) and not re.search(r'котор', v.lower()):#
        #       ищем сочетание букв кот или кош в нижнем                            но что бы небыло сочетания котор
            cat_value += 1

print(cat_value)