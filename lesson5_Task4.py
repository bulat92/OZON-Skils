file = open('diary.txt', 'a') # открытие для дозаписи

input_data = input('Введите дату в формате дд.мм.гггг(02.06.2021) |')
input_text = input('Введите текст записи |')
print(f"Вы уверены что хотите сделать запись {input_data} текст записи {input_text}? |")

answer = input("Да/Нет |")

if answer.lower() == 'да':
    file.write(f"\n{input_data} {input_text}")# запись даты и текста
    print(f"Отлично! Запись сделана")

elif answer.lower() == 'нет':
    print('Очень жаль')



file = open('diary.txt')# пофторное открытие для чтения

print(file.read())#вывод

file.close()
