def calculate_salary(gms, ic, n, b):
    
    monthly_salary = (gms / 31) * n  
    tax = (ic / 100) * monthly_salary  
    net_salary = monthly_salary - tax + b  
    print("Your gross monthly salary is :",gms,"rupees")
    print("Income tax percentage :",ic,"%")
    print("You got a bonus of",b,"rupees")
    print("You were present for",n,"days in this month")
    print("Your net salary is :",round(net_salary, 2),"rupees")

print("Enter employee type:")
ty = input("Enter 'p' for permanent and 'c' for contract-based: ").lower()

if ty == 'p':
    gms = 50000  
    ic = 5  
elif ty == 'c':
    gms = 30000  
    ic = 3  
else:
    print("Invalid input")
    exit(0)

n = int(input("Enter number of days present (max 31): "))
if n < 0 or n > 31:
    print("Invalid input for days present")
    exit(0)

b = float(input("Enter bonus if any, else enter 0: "))
if b < 0:
    print("Invalid input for bonus")
    exit(0)

calculate_salary(gms, ic, n, b)
