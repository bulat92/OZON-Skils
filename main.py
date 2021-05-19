import re

while True: #
    def get_born_year():
        born_year = re.sub('\D','', input("В каком году вы родились?"))# Все символы кроме цифр отфильтруются здесь

        if born_year: # True если значение не пустое

            return int(born_year)

        else:
            print("Не верная дата! Введите дату заново")
            return get_born_year()

    def get_settlement_date(born_year):
        settlement_date = re.sub('\D','', input("К какому году нужно посчитать возраст?")) # Все символы кроме цифр отфильтруются здесь

        if settlement_date: # True если значение не пустое

            if int(settlement_date) > born_year: # проверка расчетной даты что бы она не была меньше даты рожднеия
                return int(settlement_date)

            else:
                print("Не верная дата! Расчетная дата не может быть меньше даты рождения")
                return get_settlement_date(born_year)
        else:
            print("Не верная дата! Введите дату заново")
            return get_settlement_date(born_year)

    born_year = get_born_year()

    settlement_date = get_settlement_date(born_year) # Передается дата рождения для проверки

    print(settlement_date - born_year)
