from pick import pick
from functions.resultFunction import resultFunction

def geschwindigkeitenMenu():

    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "kmh->ms", "ms->kmh", "kmh->mph", "mph->kmh", "kmh->knt", "knt->kmh"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        return False

    input1 = float(input("Input des Geschwindigkeit in " + str(str(option).split("->")[0] + ": ")))

    match index:

        case 1:
            result = input1 / 3.6
            calculation = "Umrechnung von Kilometer pro Stunde in Meter pro Sekunde."
        
        case 2:
            result = input1 * 3.6
            calculation = "Umrechnung von Meter pro Sekunde in Kilometer pro Stunde."

        case 3:
            result = input1 / 1.609
            calculation = "Umrechnung von Kilometer pro Stunde in Meilen pro Sekunde."
        
        case 4:
            result = input1 * 1.609
            calculation = "Umrechnung von Meilen pro Sekunde in Kilometer pro Stunde."

        case 5:
            result = input1 / 1.852
            calculation = "Umrechnung von Kilometer pro Stunde in Knoten."
        
        case 6:
            result = input1 * 1.852
            calculation = "Umrechnung von Knoten in Kilometer pro Stunde."


    if(resultFunction(result, calculation)):
        return True
    else:
        geschwindigkeitenMenu()
