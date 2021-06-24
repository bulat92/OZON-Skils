import random

p = lambda x: print(x)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_class(self):
        return self.name, self.surname

    def __str__(self):
        return ' '.join(self.print_class())


class Professor(Person):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course

    def test_stugents(self, arr):
        [[[[v.set_test_score(random.randrange(0, 10)), p(v)] for v in arr], p('')] for i in range(2)]
        # тут два цикла в одной строке| внешний запускается 2 раза| внутренний проходя по массиву классов вызывает метод
        # set_test_score с random.randrange(0, 10) значением
    def __str__(self):
        return f'Преподаватель: {self.name} {self.surname} читает курс по {self.course}'


class Student(Person):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.score_array = []

    def set_test_score(self, new_score):
        self.score_array.append(new_score)

    def __str__(self):
        return f'Студент: {self.name} {self.surname} изучает курс по {self.course}. Его оценки {self.score_array}'


Gordon = Professor('Гордон', 'Фриман', 'Физике')
Duplicate = Student('Кейт', 'Ча', Gordon.course)
Invincible = Student('Марк', 'Грейсон', Gordon.course)
Black_Samson = Student('Маркус', 'Гримшоу', Gordon.course)
One_Punch_Man = Student('Сайтама', 'Ваншотович', Gordon.course)

p(Gordon)
p('')

Gordon.test_stugents([Invincible, Duplicate, Black_Samson, One_Punch_Man])


