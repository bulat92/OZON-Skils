class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_class(self):
        return self.name, self.surname

    def __str__(self):
        return ' '.join(self.print_class())


Gordon = Person('Gordon', 'Freeman')
Mark = Person('Mark', 'Grayson')

print(Gordon)
print(Mark)
