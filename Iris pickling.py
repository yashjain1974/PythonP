'''For Pickling object we use this code'''
import requests
import time
import pickle
try:
 url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
 a=requests.get(url)
 c=a.text
 l1=c.split("\n")   #or we use c.splitlines()
 list2=[[item] for item in l1 if len(item)!=0]
 print("Pickling your Data.....")
 with open("iris.pkl","wb") as f:
    pickle.dump(list2,f)
 '''For reading Pickle file we use below code'''
 time.sleep(3)
 print("pickling Completed......")
 print("your pickled Data is:-")
 with open("iris.pkl","rb") as f:
    q=pickle.load(f)
    print(q)
except Exception as e:
    print("\nOnline Pickle......")
    print("Something went Wrong")
    print(e)
    print("\n\nOffline pickle.....")
    with open("iris.pkl", "rb") as f:
        print(pickle.load(f))



