# HEALTHY PROGRAMMER (9am-5pm)
# WATER - water.mp3 3.5 l in 9am to 5pm time then he/she would input- every 30 mins
# Y for drank and N for not drank and then enter that in a text file log with time
# EYES - eyes.mp3 every 30mins in 9am to 5pm time then he/she would input - 25mins
# #Y for done and N for not done and then enter that in a text file log with time
# PHYSICAL ACTIVITY- physical.mp3 every 45mins in 9am to 5pm time then he/she would input -45mins
# #Y for done and N for not done and then enter that in a text file log with time
# pygame module for playing mp3 - 60 mins
# you will have to manage the clashes between the remainders play at same time

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