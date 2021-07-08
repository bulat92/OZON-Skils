import pyowm
from tkinter import ttk
import tkinter as tk


window = tk.Text()
box_button = tk.Frame()

choice_city = ttk.Combobox(values=['Moscow,RU', 'Kazan,RU', 'Sankt Petersburg,RU', 'Ufa,RU'])

def get_weather_Func():
    pass

show_weather = tk.Button(master=box_button, text='Показать погоду', command=get_weather_Func)


window.grid()
box_button.grid(row=1, column=0)
choice_city.grid(row=1, column=0)

window.mainloop()

