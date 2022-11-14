from pick import pick
from calcs.einheiten.druck import druckMenu
from calcs.einheiten.geschwindigkeiten import geschwindigkeitenMenu

from calcs.einheiten.laengen import laengenMenu
from calcs.einheiten.temperatur import temperaturMenu

def einheitenMenu():
    
    title = "Welche Umrechnung soll es sein?"
    options = ["Back", "Längen", "Geschwindigkeiten", "Druck", "Temperatur"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    match index:
        case 0:
            return

        case 1:
            menu = laengenMenu()

        case 2:
            menu = geschwindigkeitenMenu()
            
        case 3:
            menu = druckMenu()

        case 4:
            menu = temperaturMenu()
    
    if(menu):
        return
    else:
        einheitenMenu()
