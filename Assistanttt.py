
from win32com.client import Dispatch
i=input("Enter What I speak")
speak=Dispatch("SAPI.SpVoice")
speak.Speak(i)
speak.Speak("Hi I am Alaska. I am a window Assistant. My hobby is speaking")
speak.Speak("what is your name")
a=input("what is your name")

speak.Speak(f" Hi {a} bro, welcome to Assistant")