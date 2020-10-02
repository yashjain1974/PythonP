import random
a=int(input("enter number"))
b=[]
s=set(b)
for i in range(0,a):
    c=int(round(random.random()*100))
    s.add(c)
h=s
print(h)

# n=0
# while(n<10):
#     d = round(random.random() * 100)
#     print(d)
#     n+=1
#     g=int(input("enter 1 or 0"))
#     if g==1:
#      if d==h:
#       h.union(d)
#      print(s)
#     elif g==0:
#         exit()

