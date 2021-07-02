import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])


if not filepath:
    return
txt_edit.delete("1.0", tk.END)
with open(filepath, "r") as input_file:
    text = input_file.read()
txt_edit.insert(tk.END, text)
window.title(f"Текстовый редактор - {filepath}")


def save_file():
    filepath = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
                                 )


if not filepath:
    return
with open(filepath, "w") as output_file:
    text = txt_edit.get("1.0", tk.END)
output_file.write(text)
window.title(f"Текстовый редактор - {filepath}")

window = tk.Tk()

txt_edit = tk.Text()
txt_edit.pack()
fr_buttons = tk.Frame()

fr_buttons.pack(fill=tk.X)
btn_submit = tk.Button(master=fr_buttons, text="Загрузить", command=open_file)
btn_submit.pack(side=tk.LEFT)
btn_clear = tk.Button(master=fr_buttons, text="Сохранить", command=save_file)
btn_clear.pack(side=tk.RIGHT)
window.mainloop()