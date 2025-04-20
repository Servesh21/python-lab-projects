
import mymodule


check = True


while check:
    print("Operations")
    print("1. Square")
    print("2. Factorial")
    print("3. Prime")
    print("4. Exit")
    n = input("Enter your choice: ")
    if n == '1':
        a = float(input("Enter a number: "))
        k = mymodule.powNumber(a)
        print("The square of", a, "is", k)
    elif n == '2':
        a = int(input("Enter a number: "))
        f = mymodule.factorial(a)
        print("The factorial of", a, "is", f)
    elif n == '3':
        a = int(input("Enter a number: "))
        if mymodule.primeNumber(a):
            print(a, "is a prime number")
        else:
            print(a, "is not a prime number")
    elif n == '4':
        print("Exiting..")
        check = False
    else:
        print("Invalid input")
