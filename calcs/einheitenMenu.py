from pick import pick

from calcs.einheiten.laengen import laengenMenu

def einheitenMenu():
    
    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "Längen", "Geschwindigkeiten", "Volumen"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    if(index == 0):
        return

    if(index == 1):
        menu = laengenMenu()

    
    if(menu):
        return
    else:
        einheitenMenu()
