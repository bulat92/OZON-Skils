from tkinter import ttk
from datetime import date
from tkinter import *
import tkinter as tk
import requests, pickle

cities = {'Moscow': 'Москве', 'Kazan': 'Казане', 'Sankt Petersburg': 'Санкт-Петербурге', 'Ufa': 'Уфе'}

api_keys = '8abe2497f6167e77e46f4d329a58e800'

window = tk.Tk()
window.title('Final project')
window.geometry('500x500')

text_Label = tk.Label(justify=LEFT)
text_Label.pack()

row_two = tk.Frame()
row_two.pack(side=tk.BOTTOM, fill=tk.X)

row = tk.Frame()
row.pack(side=tk.BOTTOM, fill=tk.X)

input_city = Entry(master=row_two)
input_city.pack(side=tk.LEFT, pady=10, padx=10)

choice_city = ttk.Combobox(master=row, values=['Выберите город здесь', 'Moscow', 'Kazan',
                                                      'Sankt Petersburg', 'Ufa'])
choice_city.pack(side=tk.LEFT, pady=10, padx=10)
choice_city.current(0)

def get_weather_Func():

    if choice_city.current() > 0:
        respons = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={choice_city.get()}'
                               f'&units=metric&lang=ru&appid={api_keys}').json()
        text_Label['text'] += (f"{date.today().strftime('%d.%m.%Y')} Сегодня температура в "
                                f"{cities[choice_city.get()]} {respons['main']['temp']}. "
                                f"На улице {respons['weather'][0]['description']}\n")
    if input_city.get() != '':
        respons = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input_city.get()}'
                               f'&units=metric&lang=ru&appid={api_keys}').json()
        text_Label['text'] += (f"{date.today().strftime('%d.%m.%Y')} Сегодня температура в "
                                f"{cities[choice_city.get()]} {respons['main']['temp']}. "
                                f"На улице {respons['weather'][0]['description']}\n")
    choice_city.current(0)

def save_weather_Func():
    file = open(f"weather.dat", 'wb')  # запись в .дат файлы
    pickle.dump(text_Label['text'], file)
    text_Label['text'] = ''
    file.close()

show_weather = tk.Button(master=row, text='Показать погоду', command=get_weather_Func)
show_weather.pack(side=tk.RIGHT, pady=10, padx=10)

save_weather = tk.Button(master=row_two, text='Сохранить данные', command=save_weather_Func)
save_weather.pack(side=tk.RIGHT, pady=10, padx=10)

window.mainloop()