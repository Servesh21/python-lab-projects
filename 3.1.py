def fine(delay,damage,p):   
    f = (delay * p)+((damage * p))
    return f
days = int(input("How many days book was kept with the student : "))

print("Is the book damaged?")
z = input("Enter 'Y' for yes and 'N' for no : ")
if(z.lower() == 'y'):
    damage = float(input("Enter percentage of damage to the book : "))
elif(z.lower() == 'n'):
    damage = 0 
else:
    print("Invalid input")

print("Enter book type : ")
ty = input("Enter 'R' for reference book and 'B' for book bank : ")
if(ty.lower() == 'r'):
    p = 50
    v = 'Reference book.'
elif(ty.lower() == 'b'):
    p = 20
    v = 'Normal Book.'
else:
    print("Invalid input")
if(days < 10 and damage == 0):
    print("No fine")
elif(damage > 0 and (days - 10) < 0):
    k = fine(0,damage,p)
    print("You borrowed a",v,"The book was",damage,"% damaged. So the total fine is",k,"rupees.")
else:
    k = fine((days - 10),damage,p)
    print("You borrowed a",v,"The book was",damage,"% damaged and you returned it",(days-10),"days late. So the total fine is",k,"rupees.")
