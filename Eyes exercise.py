import time
from datetime import datetime
from pygame import mixer
def eyes(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    while(True):
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"\n\n{msg}{datetime.now()}\n")
if __name__ == '__main__':
    initialize_eyes = time.time()

    eyes_sec=1200
    while True:
        if time.time() - initialize_eyes > eyes_sec:
            print("Type ok to stop the alarm")
            eyes("alarm_clock.mp3", "ok")
            initialize_eyes = time.time()
            log_now("Eyes physically exercise at : ")
        a = str(input("For quit alarm Type quit or no\n"))
        if (a=="quit"):
            break
        elif(a=="no"):
            continue