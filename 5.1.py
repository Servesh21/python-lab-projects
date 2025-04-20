class EmpClass:

    def __init__(self,name="Rohan",age=32):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        
print("Employee 1")
emp1 = EmpClass()
emp1.display()

emp2 = EmpClass("Kaplesh",23)
print("Employee 2")
emp2.display()

print("Enter details for employee 3 : ")
name = input("Enter name of employee 3 : ")
age = input("Enter age of employee 3 : ")
emp3 = EmpClass(name,age)
print("Employee 3")
emp3.display()

print("Employee 4")
emp4 = EmpClass(age=10)
emp4.display()

print("Employee 5")
emp5 = EmpClass("krisshh")
emp5.display()
