import re

all_salary = int(re.sub('\D', '', input("Введите первую сумму?")))
all_salary += int(re.sub('\D', '', input("Введите вторую сумму?")))
all_salary += int(re.sub('\D', '', input("Введите третью сумму?")))

print(all_salary//3)

