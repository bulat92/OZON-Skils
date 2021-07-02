import os, json
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def load_Func(): # функция загрузки последнего сохронения если такая есть
    if os.path.exists('settings.json'):#
        with open('settings.json') as f_json:# проверяет json файл
            f_json = json.loads(f_json.read()).split(':')
            if os.path.exists(f'{f_json[1]}:{f_json[2]}'):  #проверяет последний сохраненный файл если он есть
                                                            # то открывает его
                open_func(f'{f_json[1]}:{f_json[2]}')


def save_button_Func(): # кнопка сохранения
    file_name = asksaveasfilename(filetypes=[("Текстовые документы", "*.txt"), ("Все файлы", "*.*")], defaultextension="txt")

    if not file_name:
        return
    else:
        file = open(file_name, "w")
        file.write(text_area.get(1.0, tk.END))
        window.title(os.path.basename(file_name) + ' - Notepad')
        with open(f'settings.json', 'w') as f_json: # запись json
            json.dump(f'{os.path.basename(file_name)}:{file_name}', f_json)
        file.close()

def open_button_Func(): # кнопка открыть
    file_name = askopenfilename(filetypes=[("Текстовые документы", "*.txt"), ("Все файлы", "*.*")])
    open_func(file_name)

def open_func(file_name): # функция открыть. Функция открытия разделена на 2 части для разных способов открытия файла
    if not file_name:
        return
    else:
        file = open(file_name, "r")
        window.title(os.path.basename(file_name) + ' - Notepad')
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, file.read())
        file.close()

window = tk.Tk()

text_area = tk.Text()
text_area.pack()

box_button = tk.Frame()

box_button.pack(fill=tk.X)

saveB   = tk.Button(master=box_button, text="Сохранить", command=save_button_Func)# создания кнопки сохранения
uploadB = tk.Button(master=box_button, text="Загрузить", command=open_button_Func)# создания кнопки загрузки

uploadB.pack(side=tk.LEFT)
saveB.pack(side=tk.RIGHT)
load_Func()
window.mainloop()