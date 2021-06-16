from lesson8_task1 import requester_func

soup = requester_func()

dict = {} # итоговый словарь

for elem in soup.find_all('div', class_='tab_item_content'): # находим по div и нужному классу блоки div содержащие контент

    name_game, zero, labels = elem.text.strip().split('\n') #вычищаем пробелы из текста И переносом строк делим строки для присваивания

    dict.update({name_game: labels.strip()}) #доавить в словарь

if __name__ == '__main__':
    for k, v in dict.items():

        print(f"{k}\n{v}\n")
