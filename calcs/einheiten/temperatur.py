from pick import pick
from functions.resultFunction import resultFunction

def temperaturMenu():

    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "C->F", "F->C", "C->K", "K->"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        return False

    input1 = float(input("Input des Temperatur in " + str(str(option).split("->")[0] + ": ")))

    match index:

        case 1:
            result = (input1 * 9/5) + 32
            calculation = "Umrechnung von Grad Celsius in Grad Fahrenheit."
        
        case 2:
            result = (input1 - 32) * 5/9
            calculation = "Umrechnung von Grad Fahrenheit in Grad Celsius."

        case 3:
            result = input1 - 273
            calculation = "Umrechnung von Grad Celsius in Kelvin."
        
        case 4:
            result = input1 + 273
            calculation = "Umrechnung von Kelvin in Grad Celsius."


    if(resultFunction(result, calculation)):
        return True
    else:
        temperaturMenu()
