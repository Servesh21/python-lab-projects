n=int(input("Enter number of intergers in the list : "))
list = []
print("Enter integers in the list : ")
for i in range(n):
    list.append(int(input()))

print("Entered list is :",list)
x = int(input("Enter element you want to search for : "))
ind = []
j = 0
c = 0
for i in list:
    if(i == x):
        c += 1
        ind.append(j)
    j += 1
if(c == 0):
    print(f"{x} is not present in the list")
else:
    print(f"{x} occurs in the list {c} times at index locations {ind}")
