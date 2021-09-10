import math
import random

def calc():
    result = "error: input out of range"
    calc0 = 0
    calcsim = 0
    calckom = 0
    calctri = 0
    calcconv = 0
    calcconlength = 0
    calc3 = 0
    input1 = 0
    input2 = 0
    input3 = 0
    alpha = 0
    beta = 0
    gamma = 0
    a = 0
    b = 0
    c = 0

    calc0 = float(input("[0:exit] [1:einfach] [2:komplex] [3:trigonometrie] [4:umrechnung] [5:grafiktaschenrechner]"))

    if(calc0 == float(42)):
        def rock_paper_scissors():
            print("Welcome to Rock Paper Scissors")
            print("Please choose:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Quit")
            user_choice = int(input("Enter your choice: "))
            while user_choice != 4:
                computer_choice = random.randint(1, 3)
                if user_choice == computer_choice and user_choice == 1:
                    print("Tie! We both chose rock!")
                if user_choice == computer_choice and user_choice == 2:
                    print("Tie! We both chose paper!")
                if user_choice == computer_choice and user_choice == 3:
                    print("Tie! We both chose scissors!")
                elif user_choice == 1 and computer_choice == 2:
                    print("You lose! I chose paper and you rock!")
                elif user_choice == 1 and computer_choice == 3:
                    print("You win! You chose rock and i scissors!")
                elif user_choice == 2 and computer_choice == 1:
                    print("You win! You chose paper and i rock!")
                elif user_choice == 2 and computer_choice == 3:
                    print("You lose! I chose scissors and you paper!")
                elif user_choice == 3 and computer_choice == 1:
                    print("You lose! I chose rock and you scissors!")
                elif user_choice == 3 and computer_choice == 2:
                    print("You win! You chose scissors and i paper!")
                print("Please choose:")
                print("1. Rock")
                print("2. Paper")
                print("3. Scissors")
                print("4. Quit")
                user_choice = int(input("Enter your choice: "))
            print("Thanks for playing")
            calc()

        rock_paper_scissors()

    if(calc0 == float(1)):
        calcsim = float(input("[1:addieren] [2:subtrahieren] [3:multiplizieren] [4:dividieren]"))
        input1 = float(input("input1: "))
        input2 = float(input("input2: "))
    elif(calc0 == float(2)):
        calckom = float(input("[1:wurzel] [2:x^y]"))
    elif(calc0 == float(3)):
        calctri = float(input("[1:sin] [2:cos] [3:tan] [4:Dreieck]"))
        input1 = float(input("input1: "))
    elif(calc0 == float(4)):
        calcconv = float(input("[1:Länge] [2:Volumen]"))
    
    elif(calc0 == float(5)):
        result = "error: function not availible yet"


    if(calctri == float(4)):
        calc3 = float(input("[1:SSS] [2:SWS] [3:WSW] [4:SSW] [5:WWS]"))
    #SSS(Nur Seiten)
    if(calc3 == float(1)):
        input1 = float(input("a: "))
        input2 = float(input("b: "))
        input3 = float(input("c: "))
        alpha = float(math.degrees(math.acos(((input1 ** 2) - (input2 ** 2) - (input3 ** 2)) / ( -2 * input2 * input3))))
        beta = float(math.degrees(math.acos(((input2 ** 2) - (input1 ** 2) - (input3 ** 2)) / ( -2 * input1 * input3))))
        gamma = float(math.degrees(math.acos(((input3 ** 2) - (input2 ** 2) - (input1 ** 2)) / ( -2 * input2 * input1))))
        result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))
    #SWS(2 Seite ohne gegenüberliegenden Winkel(1))
    elif(calc3 == float(2)):
        input1 = float(input("a: "))
        input2 = float(input("beta: "))
        input3 = float(input("c: "))
        b = float(math.sqrt((input1 ** 2 + input3 ** 2) - 2 * input1 * input3 * (math.cos((input2 * math.pi / 180)))))
        alpha = float(math.degrees(math.asin(math.sin((input2 * math.pi / 180)) / b * input1))) 
        gamma = float(180 - input2 - alpha)
        result = ("\na= " + str(input1) + "\nb= " + str(b) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))
    #WSW(2 Winkel ohne gegenüberliegender Seite(1))
    elif(calc3 == float(3)):
        input1 = float(input("alpha: "))
        input2 = float(input("b: "))
        input3 = float(input("gamma: "))
        beta = float(180 - (float(input1) + float(input3)))
        a = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input1 * math.pi / 180))
        c = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input3 * math.pi / 180))

        result = ("\na= " + str(a) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(beta) + "\ngamma= " + str(input3))
    #SSW(2 Seiten mit gegenüberliegenden Winkel(1))
    #elif(calc3 == float(4)):
    #    input1 = float(input("a: "))
    #    input2 = float(input("b: "))
    #    input3 = float(input("alpha: "))
    #    beta = float(math.asin(math.sin(alpha * math.pi / 180) * input2))
    #    gamma = float(180 - input3 - beta)
    #    c = (input1 / math.sin(input3 * math.pi / 180) * math.sin(gamma * math.pi / 180)) 
    #    result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input3) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma)) """
    #WWS(2 Winkel mit gegenüberliegender Seite(1))
    elif(calc3 == float(5)):
        input1 = float(input("alpha: "))
        input2 = float(input("beta: "))
        input3 = float(input("a: "))
        gamma = float(180 - input1 - input2)
        b = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(input2 * math.pi / 180))
        c = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(gamma * math.pi / 180))
        result = ("\na= " + str(input3) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))




    if(calcconv == float(1)):
        calcconlength = float(input("[1:km->mil] [2:mil->km] [3:meter->feet] [4:feet->meter] [5:cm->zoll] [6:zoll->cm] [7:km->sm] [8:sm->km]"))
        input1 = float(input("input1: "))
    elif(calcconv == float (2)):
        calcconvol = 0
        result = "error: function not availible yet"







    if(calcsim == float(1)):
        result = input1 + input2
    elif(calcsim == float(2)):
        result = input1 - input2
    elif(calcsim == float(3)):
        result = input1 * input2
    elif(calcsim == float(4)):
        result = input1 / input2
    elif(calctri == float(1)):
        result = math.sin(input1)
    elif(calctri == float(2)):
        result = math.cos(input1)
    elif(calctri == float(1)):
        result = math.tan(input1)
    elif(calckom == float(1)):
        input1 = float(input("input1: "))
        result = math.sqrt(input1)
    elif(calckom == float(2)):
        input1 = float(input("input1: "))
        input2 = float(input("input2: "))
        result = input1 ** input2
    elif(calcconlength == float(1)):
        result = input1 / 1.609
    elif(calcconlength == float(2)):
        result = input1 * 1.609
    elif(calcconlength == float(3)):
        result = input1 * 3.281
    elif(calcconlength == float(4)):
        result = input1 / 3.281
    elif(calcconlength == float(5)):
        result = input1 / 2.54
    elif(calcconlength == float(6)):
        result = input1 * 2.54
    elif(calcconlength == float(7)):
        result = input1 / 1.852
    elif(calcconlength == float(8)):
        result = input1 * 1.852









    if(calc0 == 0): 
        exit()
    if(calc0 != 42):
        print(result)
        calc()
    

calc() 