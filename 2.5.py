print("Numbers divisible by 3,6,9")
list = [i for i in range(1,101) if (i % 3 == 0) and (i % 6 == 0) and (i % 9 == 0)]
print(list)

print("Squares")
squares = [i**2 for i in range(1, 21) if i % 2 == 0]
print(squares)
