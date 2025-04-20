n=int(input("Enter number of elements in the list : "))
l = []
print("Enter elements in the list : ")
for i in range(n):
    l.append(input())

print("Entered list is :",l)
fl = []
ch = []
i = []
b = []
no = []
for k in l:
    if k.isdigit():
        i.append(int(k))
    elif k.replace('.','',1).isdigit():
        fl.append(float(k))
    elif k.lower() == 'true' or k.lower() == 'false':
        b.append(bool(k))
    elif k.lower() == 'none':
        no.append(k)    
    else:
        ch.append(k)
print("No of elements of each data type are as follows")
print("Integers :",len(i),i)
print("Float :",len(fl),fl)
print("Boolean :",len(b),b)
print("String :",len(ch),ch)
print("None :",len(no),no)
