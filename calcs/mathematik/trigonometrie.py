import math
from pick import pick

from functions.resultFunction import resultFunction

def trigonometrieMenu():
    calculation = None
    title = "Welche Werte liegen vor?"
    options = ["Back", "SSS", "SWS", "WSW", "WWS"]

    option, index = pick(options, title, indicator='=>', default_index=1)

    match index:

        case 0:
            return False

        case 1:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            
            alpha = float(math.degrees(math.acos(((a ** 2) - (b ** 2) - (c ** 2)) / ( -2 * b * c))))
            beta = float(math.degrees(math.acos(((b ** 2) - (a ** 2) - (c ** 2)) / ( -2 * a * c))))
            gamma = float(math.degrees(math.acos(((c ** 2) - (b ** 2) - (a ** 2)) / ( -2 * b * a))))
            result = ("\na= " + str(a) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))

        case 2:
            a = float(input("a: "))
            beta = float(input("beta: "))
            c = float(input("c: "))
            
            b = float(math.sqrt((a ** 2 + c ** 2) - 2 * a * c * (math.cos((beta * math.pi / 180)))))
            alpha = float(math.degrees(math.asin(math.sin((beta * math.pi / 180)) / b * a))) 
            gamma = float(180 - beta - alpha)
            
            result = ("\na= " + str(a) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))

        case 3:
            alpha = float(input("alpha: "))
            b = float(input("b: "))
            gamma = float(input("gamma: "))
            
            beta = float(180 - (float(alpha) + float(gamma)))
            a = float(b / math.sin(beta * math.pi / 180) * math.sin(alpha * math.pi / 180))
            c = float(b / math.sin(beta * math.pi / 180) * math.sin(gamma * math.pi / 180))

            result = ("\na= " + str(a) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))

        case 4:
            gamma = float(input("alpha: "))
            beta = float(input("beta: "))
            a = float(input("a: "))
            
            gamma = float(180 - gamma - beta)
            b = float(a / math.sin(gamma * math.pi / 180) * math.sin(beta * math.pi / 180))
            c = float(a / math.sin(gamma * math.pi / 180) * math.sin(gamma * math.pi / 180))
            
            result = ("\na= " + str(a) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(gamma) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))

    if(resultFunction(result, calculation)):
        return True
    else:
        trigonometrieMenu()

