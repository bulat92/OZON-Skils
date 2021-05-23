import re
import random

deposit = 10000
journal = []
game_number = 0

print("Добро пожаловать в виртуальное казино! Ваш начальный депозит 10000")

while deposit > 0:

    unknown_number = random.randrange(2, 12)

    answer = re.sub('\D', '', input("Число загадано попробуйте его отгадать! Введите значение от 2 до 12! |"))

    if answer:
        answer = int(answer)

        if answer >= 2 and answer <= 12:

                game_number += 1
                print(game_number)

                if answer == unknown_number:
                    deposit += 1000
                    print("Число отгадано! Загаданное число " + str(unknown_number))
                    print("Размер вашего депозита " + str(deposit))
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

                    journal.append("Игра загадала: " + str(unknown_number) + ", моя попытка: " + str(
                        game_number) + ", на счету: "+str(deposit))

                else:
                    deposit -= 1000
                    print("Число не отгадано! Загаданное число " + str(unknown_number))
                    print("Размер вашего депозита " + str(deposit))
                    print("-----------------------------------------------------------------------")
                    journal.append("Игра загадала: " + str(unknown_number) + ", моя попытка: " + str(
                        game_number) + ", на счету: " + str(deposit))
        else:
            print("Введенное число не соответствует заданному промежутку!")
            print("***********************************************************************")
    else:
       print("Введенное число не соответствует заданному промежутку!")
       print("***********************************************************************")

print("Игра закончена вы проиграли весь ваш депозит!")
print("00000000000000000000000000000000000000000000000000000000000000000000000")

for i in range(len(journal)):
    print(journal[i])