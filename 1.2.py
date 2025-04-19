start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
print(f"The prime numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
