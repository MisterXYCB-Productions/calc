from pick import pick
from functions.resultFunction import resultFunction

def laengenMenu():

    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "km->mil", "mil->km", "meter->feet", "feet->meter", "cm->zoll", "zoll->cm", "km->sm", "sm->km"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        return False

    input1 = float(input("Input der Länge in " + str(str(option).split("->")[0] + ": ")))

    match index:

        #km->mil
        case 1:
            result = input1 / 1.609
            calculation = "Umrechnung von Kilometern in Meilen."
        
        #mil->km
        case 2:
            result = input1 * 1.609
            calculation = "Umrechnung von Meilen in Kilometer."

        #meter->feet
        case 3:
            result = input1 * 3.281
            calculation = "Umrechnung von Meter in Fuß."

        #feet->meter
        case 4:
            result = input1 / 3.281
            calculation = "Umrechnung von Fuß in Meter."

        #cm->zoll
        case 5:
            result = input1 / 2.54
            calculation = "Umrechnung von Centimeter in Zoll."
        
        #zoll->cm
        case 6:
            result = input1 * 2.54
            calculation = "Umrechnung von Zoll in Centimeter."
        
        #km->sm
        case 7:
            result = input1 / 1.852
            calculation = "Umrechnung von Kilometern in Seemeilen."

        #sm->km
        case 8:
            result = input1 * 1.852
            calculation = "Umrechnung von Seemeilen in Kilometer."


    if(resultFunction(result, calculation)):
        return True
    else:
        laengenMenu()
