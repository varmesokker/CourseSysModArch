class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.__salary = salary
        self.project = project

    def show(self):
        """
        Hallo
        :return:
        """
        print("Name: ", self.name, 'Salary: ', self.__salary)


emp = Employee('Jessa', 8000, 'NPL')
emp1 = Employee('Ole', 1000000, 'FiV')

print(emp.name)
print(emp._Employee__salary)
print(emp.project)
emp.show()




"""


class Company:
    def __init__(Self):
        # Protected member
        self._project = "NLP"


class Employee(Company):
    def __init__(self, name):
        self.name = name
        self.__salary = salary
        self.project = project

    def show(self):
        print("Name: ", self.name, 'Salary: ', self.__salary)


c = Employee('Jessica')
c.show()

"""