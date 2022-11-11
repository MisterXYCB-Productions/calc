from pick import pick
from functions.resultFunction import resultFunction

def laengenMenu():

    title = "Welche Umrechnung soll es sein?"
    options = ["km->mil", "mil->km", "meter->feet", "feet->meter", "cm->zoll", "zoll->cm", "km->sm", "sm->km"]

    option, index = pick(options, title, indicator='=>', default_index=0)

    input1 = int(input("Input der Länge in " + str(str(option).split("->")[0])))

    #km->mil
    if(index == 1):
        result = input1 / 1.609
        resultFunction(result)
        return
    
    #mil->km
    elif(index == 2):
        result = input1 * 1.609
        resultFunction(result)
        return

    #meter->feet
    elif(index == 3):
        result = input1 * 3.281
        resultFunction(result)
        return

    #feet->meter
    elif(index == 4):
        result = input1 / 3.281
        resultFunction(result)
        return

    #cm->zoll
    elif(index == 5):
        result = input1 / 2.54
        resultFunction(result)
        return
    
    #zoll->cm
    elif(index == 6):
        result = input1 * 2.54
        resultFunction(result)
        return
    
    #km->sm
    elif(index == 7):
        result = input1 / 1.852
        resultFunction(result)
        return
    
    #sm->km
    elif(index == 8):
        result = input1 * 1.852
        resultFunction(result)
        return
    
