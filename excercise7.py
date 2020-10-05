# HEALTHY PROGRAMMER 

from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_physical = time()
    watersecs = 30*60
    eyessecs= 25*60
    physecs= 60*60

    while True:
        if time()- init_water > watersecs:
            print("Time to Drink water. Enter Y if already drank.\n")
            musicloop("water.mp3", "Y")
            init_water = time()
            log_now("Drank water at")

        if time()- init_eyes > eyessecs:
            print("Time to do eye exercise. Enter Y if already done.\n")
            musicloop("eyes (online-audio-converter.com).mp3", "Y")
            init_eyes = time()
            log_now("Done eye exercise at")

        if time()- init_physical > physecs:
            print("Time to do physical exercise. Enter Y if already done.\n")
            musicloop("physical (online-audio-converter.com).mp3", "Y")
            init_physical = time()
            log_now("Done physical exercise at")

        if input()== "quit":
            break
