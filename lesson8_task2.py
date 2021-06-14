from lesson8_task1 import requester_func as requester_func #

soup = requester_func()

dict = {} # итоговый словарь

for elem in soup.find_all('div', class_ = 'tag_count_button'): # находим по div и нужному классу блоки div содержащие контент

    name_genre, number = elem.text.strip().split('\n') #вычищаем пробелы из текста И переносом строк делим строки для присвайвания

    dict.update({name_genre: number}) #доавить в словарь

if __name__ == '__main__':
    for k, v in dict.items():

        print(f"{k}\n{v}\n")
