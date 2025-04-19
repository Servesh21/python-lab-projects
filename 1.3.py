num = int(input("Enter a number : "))
num1 = num
add = 0
print("The reverse of number", num, "is ", end='')
while(num1 != 0):
    i = num1 % 10
    print(i, end='')
    num1 //= 10
