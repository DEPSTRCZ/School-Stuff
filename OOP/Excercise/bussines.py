
class Bussines:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.employee = []
        self.branch = []
        self.positions = []

class Employee:
    def __init__(self, name, surname, age, salary, position, branch):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.position = position
        self.branch = branch

    def change_branch(self, branch):
        self.branch.remove_employee(self)
        self.branch = branch
        branch.add_employee(self)

    def change_position(self, position):
        self.position.remove_employee(self)
        self.position = position
        position.add_employee(self)7

    def fire(self):
        self.branch.remove_employee(self)
        self.position.remove_employee(self)
        bussines.employees.remove(self)
    

class Branch:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.add_employees = []

    def add_employee(self, employee):
        self.employee.append(employee)
        bussines.employees.append(employee)

    def remove_employee(self, employee):
        try:
            self.employee.remove(employee)
            bussines.employees.remove(employee)
        except:
            return "Employee not found"
    


class Position:
    pass

bussines = Bussines("Brambor s.r.o", "Praha 5", "+420 000 000 000")
#while True:
#    try:
#        pass
#    except KeyboardInterrupt:
#        exit()

print(arr[0].name)