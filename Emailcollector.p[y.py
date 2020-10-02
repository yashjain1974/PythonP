import re
str='''
Name=yash
email=yash19@gmail.com
cast=jain
email2=garvit19@gmail.com
email4=hindi@gmail.com
email13=jainagysguy@gmail.com
hobby =cricket
'''
email=re.findall(r'[\w.]+[@{1}][\w]+[.][\w.]+',str)
emails=email
print(emails)
with open("Email.txt","w") as f:
 j=0
 for email in emails:
  j+=1
  f.write(f'{j} {email}\n')



