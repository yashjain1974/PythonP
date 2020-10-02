import random
a=round(random.random()*100)
list=[20,30,40,10,60,50,70,80,90,100]
print(a)
for item in list:
 if item==a:
  list.remove(a)
  print(list)




