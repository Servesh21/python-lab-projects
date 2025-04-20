def addlist(L1,L2):
    L3=[]
    L3 = L1 + L2
    return L3

n1 = int(input("Enter number of elements in list 1 : "))
L1 = []
print("Enter elements of list 1 : ")
for i in range(0,n1):
    L1.append(input())
print("First list is :",L1)
n2 = int(input("Enter number of elements in list 2 : "))
L2 = []
print("Enter elements of list 2 : ")
for i in range(0,n2):
    L2.append(input())
print("Second list is :",L2)
L3 = []
L3 = addlist(L1,L2)
print("The new list is :",L3)
