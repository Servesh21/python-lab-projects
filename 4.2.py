try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("Result of division:", z)
    
    mylist = [1, 2, 3]
    index = int(input("Enter an index to access the list: "))
    print("Element at index", index, "is", mylist[index])
    
    print("Value of undefined variable is:", undefined_var)


except ZeroDivisionError:
    print("You cannot divide by zero.")


except IndexError:
    print("List index out of range.")


except NameError:
    print("You are using an undefined variable.")


except Exception as e:
    print("Some other error occurred:", e)


