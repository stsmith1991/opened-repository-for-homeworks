class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)
        self.__income = {wage: bonus}

    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surname}.')

    def get_total_income(self):
        return self.__income


sohowitshouldnamed = Position('Духаст', 'Вячеславович', 'manager', 200, 50)
sohowitshouldnamed.get_full_name()
print(f'Его зарплата и бонус составляют соответственно:{sohowitshouldnamed.get_total_income()}')
