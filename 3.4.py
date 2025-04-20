def modify_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    return lst

n = int(input("Enter the number of elements in the list: "))
L = []
print("Enter elements:")
for i in range(n):
    L.append(int(input()))
print("Original list:", L)
L = modify_list(L)
print("Modified list:", L)
