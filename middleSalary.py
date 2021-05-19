import re
all_salary = 0

for index in range(3):
    all_salary += int(re.sub('\D', '', input("Введите сумму №" + str(index + 1) + " ")))

print(all_salary//3)

