from pick import pick
from functions.resultFunction import resultFunction

def druckMenu():

    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "bar->pascal", "pascal->bar"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        return False

    input1 = float(input("Input des Drucks in " + str(str(option).split("->")[0] + ": ")))

    match index:

        case 1:
            result = input1 * 100000
            calculation = "Umrechnung von Bar in Pascal."
        
        case 2:
            result = input1 / 100000
            calculation = "Umrechnung von Pascal in Bar."


    if(resultFunction(result, calculation)):
        return True
    else:
        druckMenu()
