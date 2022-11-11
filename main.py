import math
import random
from pick import pick
from calcs.rps import rps
from calcs.einheiten.laengen import laengenMenu

def startUp():
    index = 0

    title = "Wähle eine Art des Rechners!"
    options = ["EXIT", "MATHEMATIK", 'PHYSIK', 'EINHEITEN', "RPS"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        print("Closing Process")
        quit()

    if(index < 0 or index > 4):
        print("ERROR: CHOSEN OPTION IS NOT SUPPORTED")
        startUp()

    if(index == 1):
          print("lol")

    if(index == 2):
        print("LOL2")

    if(index == 3):
        laengenMenu() 

    if(index == 4):
        print("RPS")
        rps()

    startUp()

startUp()