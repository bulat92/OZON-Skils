from bs4 import BeautifulSoup
import requests, re

wiki = BeautifulSoup(requests.get('https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B1%D1%8C%D1%8E%D0%BB%D0%B0').text, 'html.parser') #

for elem in wiki.find_all('a'): # находим теги а
    href = elem.get('href') # получаем ссылки из тегов а

    if not(re.search(r'wikipedia.org', f"{href}")) and re.match('http', f"{href}"):# если в ссылке не встречает wikipedia.org и встречается http
        print(href)
