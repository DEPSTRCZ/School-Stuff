
class Bussines:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees_list = []
        self.branch_list = []
        self.positions_list = []

    def add_branch(self, branch):
        try:
            self.branch_list.append(branch)
        except:
            return "Branch already exist"

    def remove_branch(self, branch_name):
        for branch in self.branch_list:
            if branch.name == branch_name:
                self.branch_list.remove(branch)
                branch.delete()
        else:
            return "Branch not found"
        
    def list_branches(self):
        for i in self.branch_list:
            print(i.name)

    def list_branch(self, branch):
        for i in self.branch_list:
            if i.name == branch:
                print("Pobočka:")
                print("- Název ",i.name)
                print("- Adresa ",i.address)
                print("- Počet Zaměstnanců ",len(i.employees))
                if i.employees:
                    print(i.employees)
                break
        else:
            return "Branch not found"
        

    def add_position(self, position):
        if position.name in self.positions_list:
            return "Position already exist"
        else:
            self.positions_list.append(position)
        
    def remove_position(self, position_name):
        for pos in self.positions_list:
            if pos.name == position_name:
                self.positions_list.remove(pos)
                pos.delete()
        else:
            return "Position not found"
        
    def list_positions(self):
        for pos in self.positions_list:
            print(pos.name)

    def hire_employee(self, employee):
        self.employees_list.append(employee)

    def fire_employee(self, employee_name):
        try:
            for employee in self.employees_list:
                if employee.name == employee_name:
                    self.employees_list.remove(employee)
                    employee.fire()
        except:
            return "Employee not found"
        
    def list_employees(self, branch = None):
        print("Employees:")
        if branch is None:
            for employee in self.employees_list:
                print(employee.name)
        else:
            for employee in self.employees_list:
                if employee.branch == branch:
                    print(employee.name)
        
    
    def info_employee(self, employee_name):
        print("Employee info:")
        for employee in self.employees_list:
            if employee.name == employee_name:
                print("- Name: ",employee.name)
                print("- Surename: ",employee.surname)
                print("- Age: ",employee.age)
                print("- Salary: ",employee.salary)
                print("- Postition: ",employee.position)
                print("- Branch: ",employee.branch)
                break
        else:
            return "Employee not found"

class Employee:
    def __init__(self, name, surname, age, salary, position, branch):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.position = position
        self.branch = branch
        bussines.employees_list.append(self)

    def fire(self):
        self.branch.remove_employee(self)
        self.position.remove_employee(self)
        bussines.employees.remove(self)

class Branch:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.employees = []

    def add_employee(self, employee):
        self.employee.append(employee)
        bussines.employees.append(employee)

    def remove_employee(self, employee):
        try:
            self.employee.remove(employee)
            bussines.employees.remove(employee)
        except:
            return "Employee not found"
    
    def delete(self):
        bussines.remove_branch(self)
        del self
class Position:
    def __init__(self, name):
        self.name = name

    def delete(self):
        bussines.remove_position(self)
        del self
# Runner Optional
bussines = Bussines("Brambor s.r.o", "Praha 5")
print("1. Add branch") # OK
print("2. Remove branch") # OK
print("3. List branches") # OK
print("4. List branch") #OK 
print("5. Add position") # OK
print("6. Remove position")
print("7. List positions") #OK
print("8. Hire employee") # ok
print("9. Fire employee") # OK
print("10. List all employees  ||   List employees fro mcertain branch") #OK
print("11. List info about employee") # OK


while True:
    try:
        match int(input("action: ")):
            case 1:
                bussines.add_branch(Branch(str(input("Zadej název pobočky: ")), str(input("Zadej adresu: "))))
            case 2:
                bussines.remove_branch(str(input("Zadej název pobočky: ")))
            case 3:
                bussines.list_branches()
            case 4:
                bussines.list_branch(str(input("Zadej název pobočky: ")))
            case 5:
                bussines.add_position(Position(str(input("Zadej název pozice: "))))
            case 6:
                bussines.remove_position(str(input("Zadej název pozice: ")))
            case 7:
                bussines.list_positions()
            case 8:
                bussines.hire_employee(Employee(str(input("Zadej jméno: ")), str(input("Zadej příjmení: ")), int(input("Zadej věk: ")), int(input("Zadej plat: ")), str(input("Zadej pozici: ")), str(input("Zadej pobočku: "))))
            case 9:
                bussines.fire_employee(str(input("Zadej jméno: ")))
            case 10:
                bussines.list_employees()
            case 11:
                bussines.info_employee(str(input("Zadej jméno: ")))
    except KeyboardInterrupt:
        exit()