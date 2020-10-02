import time
from datetime import datetime
from pygame import mixer
def water(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    while(True):
        a= input()
        if a == stopper:
            mixer.music.stop()
            break
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
def physical_activity(file,stopper):
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
 initialize_water=time.time()
 initialize_eyes=time.time()
 initialize_phy=time.time()
 water_sec=2700
 eyes_sec=1800
 phy_sec=3000
 while True:
    if time.time()-initialize_water >water_sec:
        print("Type drank to stop the alarm")
        water("songs.mp3","drank")
        initialize_water = time.time()
        log_now("Water drinks at : ")
    elif time.time()-initialize_eyes > eyes_sec:
        print("Type stop to stop the alarm")
        eyes("songs2.mp3","stop")
        initialize_eyes = time.time()
        log_now("Eyes physically exercise at : ")
    elif time.time()-initialize_phy > phy_sec:
        print("Type pause to stop the alarm")
        physical_activity("songs3.mp3","pause")
        initialize_phy = time.time()
        log_now("Physical Exercise done at : ")













