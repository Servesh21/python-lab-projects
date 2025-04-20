n = int(input("Enter number of integers in the list: "))
num = []
print("Enter integers in the list:")
for i in range(n):
    num.append(int(input()))

print("Entered list is:", num)

choice = int(input("Press 1 for ascending order, Press 2 for descending order: "))

l = len(num)

for i in range(l):
    for j in range(i + 1, l):
        if (choice == 1 and num[i] > num[j]) or (choice == 2 and num[i] < num[j]):
            num[i], num[j] = num[j], num[i]

if choice == 1:
    print("List sorted in ascending order:", num)
elif choice == 2:
    print("List sorted in descending order:", num)
else:
    print("Invalid choice! Please enter 1 or 2.")
