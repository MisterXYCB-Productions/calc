from pick import pick

from calcs.mathematik.freieBerechnung import freieBerechnung
from calcs.mathematik.trigonometrie import trigonometrieMenu

def mathematikMenu():
   
    title = "Welche Form soll es sein?"
    options = ["Back", "Freie Berechnung", "Trigonometrie"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    match index:
        case 0:
            return

        case 1:
            menu = freieBerechnung()

        case 2:
            menu = trigonometrieMenu()

        case 3:
            mathematikMenu()

    if(menu):
        return
    else:
        mathematikMenu()
