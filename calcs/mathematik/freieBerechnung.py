from functions.resultFunction import resultFunction

def freieBerechnung():
    input1 = input("Was soll berechnet werden? ")

    result = eval(input1.replace("^", "**").replace("²", "**2").replace("³", "**3"))
    calculation = input1

    if(resultFunction(result, calculation)):
        return True
    else:
        freieBerechnung()

