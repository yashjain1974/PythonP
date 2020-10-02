import re
list1='''my name is yash hey yash 
this is a yash 
This is your yash'''
list2=list(list1)
print(list2)
search=re.findall(r'\w* yash+ \w*',list1)
print(search)