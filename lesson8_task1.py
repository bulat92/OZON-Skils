from bs4 import BeautifulSoup
import requests


def requester_func(): # в функций чтобы можно было вызывать
    return BeautifulSoup(requests.get('https://store.steampowered.com/genre/Free%20to%20Play/').text, 'html.parser')

if __name__ == '__main__':
    soup = requester_func()

    dict = {} # итоговый словарь

    for elem in soup.find_all('a'):
        href = elem.get('href') # получаем ссылки из тегов а

        text_from_href = elem.text.strip().replace('\n', '') # вычищаем пробелы и переносы строк из текста

        if text_from_href.replace(' ', '') != '' and 'Free To Play' in text_from_href: # если не пустой пробел и 'Free To Play' есть в строке

            dict.update({text_from_href: href})#доавить в словарь

    for k, v in dict.items():

        print(f"{k}\n{v}\n")
