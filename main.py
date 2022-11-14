import math
import random
from pick import pick
from calcs.mathematikMenu import mathematikMenu
from calcs.rps import rps
from calcs.einheitenMenu import einheitenMenu

def startUp():
    index = 0

    title = "Wähle eine Art des Rechners!"
    options = ["EXIT", "MATHEMATIK", 'PHYSIK', 'EINHEITEN', "RPS"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    match index:
        case 0:
            print("\n\nClosing Process")
            quit()

        case 1:
            mathematikMenu()

        case 2:
            print("LOL2")

        case 3:
            einheitenMenu() 

        case 4:
            print("RPS")
            rps()

    startUp()

startUp()
