with open("file.txt", "r") as f:
    data = f.read()
    print("\nApproach 1 - Read using read():")
    print(data)

with open("file.txt", "r") as f:
    print("\nApproach 2 - Read using readline():")
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

with open("file.txt", "r") as f:
    print("\nApproach 3 - Read using for loop:")
    for line in f:
        print(line, end="")
