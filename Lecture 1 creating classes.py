class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project


emp = Employee('Jessa', 8000, 'NPL')


print(emp.name)
print(emp.salary)
print(emp.project)