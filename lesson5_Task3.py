file = open('cat.txt', encoding='utf-8')# без ", encoding='utf-8'" не работало
file_readed = file.read()

cat_number = 0# число кошек в тексте

file_readed = file_readed.split('.')# в заданий сказано делить по строкам (\n) тогда одни и те же строки вылезают несколько раз
                                    # я решил делить на предложения

for st in file_readed:# цикл для предложений

    st = st.strip()# удаление пробелов в конце чтобы вывод был ровный

    for w in st.split():# цикл для слов

        if w == 'кошка':

            cat_number += 1
            print(f"{cat_number}. {st}") # вывод строки в которой нашлась кошка

print(f"Слово 'кошка' встречается {cat_number} раз!")
file.close()

