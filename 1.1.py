phy = float(input("Enter marks in physics : "))
chem = float(input("Enter marks in chemistry : "))
maths = float(input("Enter marks in mathematics : "))
bio = float(input("Enter marks in biology : "))
eng = float(input("Enter marks in english : "))
avg = (phy + chem + maths + bio + eng)/5
print("The average of marks of your five subjects is",avg)
if(avg>=90):
    print("Grade A\n[Range:90-100]")
elif(avg>=80 and avg<90):
    print("Grade B\n[Range:80-89.99]")
elif(avg>=70 and avg<80):
    print("Grade C\n[Range:70-79.99]")
elif(avg>=60 and avg<70):
    print("Grade D\n[Range:60-69.99]")
else:
    print("Fail\n[Range:0-59.99]")