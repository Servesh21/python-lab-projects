
count = 0
line_numbers = []


with open("server.txt", "r") as f:
    lines = f.readlines()


    for i, line in enumerate(lines, 1):
        if 'error' in line.lower():
            count += 1
            line_numbers.append(i)


with open("error.txt", "w") as f:
    f.write(f"Total occurrences of 'error': {count}\n\n")
    f.write("Line numbers where 'error' occurred:\n")
    for line_number in line_numbers:
        f.write(f"Line {line_number}\n")


print(f"Total occurrences of 'error': {count}")
print("Line numbers where 'error' occurred:")
for line_number in line_numbers:
    print(f"Line {line_number}")
