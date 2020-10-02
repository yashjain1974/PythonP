list1=[]

for i in range(5):
    a = int(input("Enter list values to be added"))
    list1.append(a)
list2=list1[:]
b=list1[::-1]
print(b)
list1.reverse()
print(list1)


for i in range (len(list1)//2):
        list2[i],list2[len(list2) -i -1]=list2[len(list2) -i -1],list2[i]
print(list2)
