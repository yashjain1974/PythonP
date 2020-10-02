from win32com.client import Dispatch
import requests
import json
def speak(str):
    news=Dispatch("SAPI.SpVoice")
    news.Speak(str)
def News():
    headlineurl="http://newsapi.org/v2/top-headlines?country=in&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    businessurl="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    entertainmenturl="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    healthurl="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    scienceurl="http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    sportsurl="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    technologyurl="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=2285f27d4dc3492586ab3ca5e50238be"
    print("\n.....................\Welcome to online News Speaking program\..............................\n")
    print("......................................................................Made By:-Yash Jain\n\n")
    news=int(input("Enter news Category:-\n"
                   "1.TopHeadlines\n"
                   "2.Business News\n"
                   "3.Entertainment News\n"
                   "4.Health News\n"
                   "5.Science News\n"
                   "6.Sports News\n"
                   "7.Technology News\n"))
    h = requests.get(headlineurl)
    i = h.text
    parsed = json.loads(i)
    date = parsed["articles"][0]["publishedAt"]
    print(f'Published at:-{date}\n')

    if (news==1):
        a=requests.get(headlineurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}.  {title}')
            speak(title)
    elif (news==2):
        a=requests.get(businessurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}.  {title}')
            speak(title)
    elif (news == 3):
        a = requests.get(entertainmenturl)
        b = a.text
        parsed = json.loads(b)
        for j in range(1,11):
            title = parsed["articles"][j]["title"]
            print(f'{j}. {title}')
            speak(title)
    elif (news==4):
        a=requests.get(healthurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}. {title}')
            speak(title)
    elif (news==5):
        a=requests.get(scienceurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}. {title}')
            speak(title)
    elif (news==6):
        a=requests.get(sportsurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}. {title}')
            speak(title)
    elif (news==7):
        a=requests.get(technologyurl)
        b=a.text
        parsed=json.loads(b)
        for j in range(1,11):
            title=parsed["articles"][j]["title"]
            print(f'{j}. {title}')
            speak(title)
if __name__ == '__main__':
    try:
        News()
        speak("Thank you...")
        print("\n\nThank you ")
    except Exception as e:
        print("please connect your Internet... ")
        print(e)
