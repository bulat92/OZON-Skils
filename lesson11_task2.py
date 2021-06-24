import random


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_class(self):
        return self.name, self.surname

    def __str__(self):
        return ' '.join(self.print_class())

class Student(Person):
    def __init__(self, name, surname, group_number, test_score):
        super().__init__(name, surname)
        self.group_number = group_number
        self.score_array = test_score

    def set_test_score(self, new_score):
        self.score_array.append(new_score)

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, группа {self.group_number}, оценки {self.score_array}"


Gordon = Student('Gordon', 'Freeman', 'resistance', [random.randrange(0, 5) for i in range(10)])
Mark = Student('Mark', 'Grayson', 'ГР-01', [random.randrange(0, 5) for i in range(10)])
Duplicate = Student('Кейт', 'Ча', 'ГР-01', [random.randrange(0, 5) for i in range(10)])
Black_Samson = Student('Маркус', 'Гримшоу', 'ГР-01', [random.randrange(0, 5) for i in range(10)])
One_Punch_Man = Student('Сайтама', 'Ваншотович', 'ГР-01', [random.randrange(0, 5) for i in range(10)])

print(Gordon)
print(Mark)
print(Duplicate)
print(Black_Samson)
print(One_Punch_Man)

