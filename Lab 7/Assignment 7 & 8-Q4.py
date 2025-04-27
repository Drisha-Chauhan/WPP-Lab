class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee(input("Enter first employee name: "), int(input("Enter salary: ")))

emp2 = Employee(input("Enter second employee name: "), int(input("Enter salary: ")))

emp3 = emp1 + emp2

print("Combined Employee:", emp3.name, "with salary", emp3.salary)

print(f"{emp1.name} earns more" if emp1 > emp2 else f"{emp2.name} earns more")
