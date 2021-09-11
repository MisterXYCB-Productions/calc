import math
import random

#main menu function
def mainMenu():

    #vars
    #general
    result = "error: input out of range"
    option = 0

    #main Menu
    option = float(input("[0:exit] [1:einfach] [2:komplex] [3:trigonometrie] [4:umrechnung] [5:grafiktaschenrechner]"))

    #easter egg: 1 Rock Paper Scissors game!
    if(option == float(42)):
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
            mainMenu()

        rock_paper_scissors()

    #function to return the result
    def resultFunction(result):
        print(str(result) + "\n")
        mainMenu()

    #function for the simple math
    if(option == float(1)):
        def simpleMenu(option):
            option = float(input("[0:go back] [1:addieren] [2:subtrahieren] [3:multiplizieren] [4:dividieren]"))
            
            #go back
            if(option == float(0)):
                mainMenu()

            input1 = float(input("input1: "))
            input2 = float(input("input2: "))

            #add
            if(option == float(1)):
                result = input1 + input2
                resultFunction(result)
            
            #substract
            elif(option == float(2)):
                result = input1 - input2
                resultFunction(result)
            
            #multiplicate
            elif(option == float(3)):
                result = input1 * input2
                resultFunction(result)
            
            #divide
            elif(option == float(4)):
                result = input1 / input2
                resultFunction(result)

        simpleMenu(option)
    
    #function for complicated math
    elif(option == float(2)):
        def complicatedMenu(option):
            option = float(input("[0:go back] [1:wurzel] [2:x^y]"))

            #go back
            if(option == float(0)):
                mainMenu()

            input1 = float(input("input1: "))
            
            #squareroot
            if(option == float(1)):
                result = math.sqrt(input1)
                resultFunction(result)

            #exponential
            elif(option == float(2)):
                input2 = float(input("input2: "))
                result = input1 ** input2
                resultFunction(result)

        complicatedMenu(option)
    
    #trigonometric functions
    elif(option == float(3)):
        def trigonometricMenu(option):
            option = float(input("[0:go back] [1:sin] [2:cos] [3:tan] [4:Dreieck]"))

            #go back
            if(option == float(0)):
                mainMenu()
            
            #triangular
            elif(option == float(4)):
                def triangularMenu(option):
                    option = float(input("[1:SSS] [2:SWS] [3:WSW] [4:WWS]")) #[5:SSW]

                    #go back
                    if(option == float(0)):
                        trigonometricMenu(option)

                    #SSS(Nur Seiten)
                    elif(option == float(1)):
                        input1 = float(input("a: "))
                        input2 = float(input("b: "))
                        input3 = float(input("c: "))
                        
                        alpha = float(math.degrees(math.acos(((input1 ** 2) - (input2 ** 2) - (input3 ** 2)) / ( -2 * input2 * input3))))
                        beta = float(math.degrees(math.acos(((input2 ** 2) - (input1 ** 2) - (input3 ** 2)) / ( -2 * input1 * input3))))
                        gamma = float(math.degrees(math.acos(((input3 ** 2) - (input2 ** 2) - (input1 ** 2)) / ( -2 * input2 * input1))))
                        
                        result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))
                        resultFunction(result)
                    
                    #SWS(2 Seite ohne gegenüberliegenden Winkel(1))
                    elif(option == float(2)):
                        input1 = float(input("a: "))
                        input2 = float(input("beta: "))
                        input3 = float(input("c: "))
                        
                        b = float(math.sqrt((input1 ** 2 + input3 ** 2) - 2 * input1 * input3 * (math.cos((input2 * math.pi / 180)))))
                        alpha = float(math.degrees(math.asin(math.sin((input2 * math.pi / 180)) / b * input1))) 
                        gamma = float(180 - input2 - alpha)
                        
                        result = ("\na= " + str(input1) + "\nb= " + str(b) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))
                        resultFunction(result)
                    
                    #WSW(2 Winkel ohne gegenüberliegender Seite(1))
                    elif(option == float(3)):
                        input1 = float(input("alpha: "))
                        input2 = float(input("b: "))
                        input3 = float(input("gamma: "))
                        
                        beta = float(180 - (float(input1) + float(input3)))
                        a = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input1 * math.pi / 180))
                        c = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input3 * math.pi / 180))

                        result = ("\na= " + str(a) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(beta) + "\ngamma= " + str(input3))
                        resultFunction(result)
                    
                    #WWS(2 Winkel mit gegenüberliegender Seite(1))
                    elif(option == float(4)):
                        input1 = float(input("alpha: "))
                        input2 = float(input("beta: "))
                        input3 = float(input("a: "))
                        
                        gamma = float(180 - input1 - input2)
                        b = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(input2 * math.pi / 180))
                        c = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(gamma * math.pi / 180))
                        
                        result = ("\na= " + str(input3) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))
                        resultFunction(result)

                    #SSW(2 Seiten mit gegenüberliegenden Winkel(1))
                    #elif(option == float(5)):
                    #    input1 = float(input("a: "))
                    #    input2 = float(input("b: "))
                    #    input3 = float(input("alpha: "))
                    #    beta = float(math.asin(math.sin(alpha * math.pi / 180) * input2))
                    #    gamma = float(180 - input3 - beta)
                    #    c = (input1 / math.sin(input3 * math.pi / 180) * math.sin(gamma * math.pi / 180)) 
                    #    result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input3) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma)) """
                
                triangularMenu(option)

            input1 = float(input("input1: "))
            
            #sin
            if(option == float(1)):
                result = math.sin(input1)
                resultFunction(result)
            
            #cos
            elif(option == float(2)):
                result = math.cos(input1)
                resultFunction(result)
            
            #tan
            elif(option == float(3)):
                result = math.tan(input1)
                resultFunction(result)


        trigonometricMenu(option)

    #converison
    elif(option == float(4)):
        def conversionMenu(option):
            option = float(input("[0:go back] [1:Länge] [2:Volumen]"))
        
            #goback
            if(option == float(0)):
                mainMenu()
        
            #distances
            elif(option == float(1)):
                option = float(input("[1:km->mil] [2:mil->km] [3:meter->feet] [4:feet->meter] [5:cm->zoll] [6:zoll->cm] [7:km->sm] [8:sm->km]"))
                input1 = float(input("input1: "))

                def distancesMenu():
                    #km->mil
                    if(option == float(1)):
                        result = input1 / 1.609
                        resultFunction(result)
                    
                    #mil->km
                    elif(option == float(2)):
                        result = input1 * 1.609
                        resultFunction(result)

                    #meter->feet
                    elif(option == float(3)):
                        result = input1 * 3.281
                        resultFunction(result)

                    #feet->meter
                    elif(option == float(4)):
                        result = input1 / 3.281
                        resultFunction(result)

                    #cm->zoll
                    elif(option == float(5)):
                        result = input1 / 2.54
                        resultFunction(result)
                    
                    #zoll->cm
                    elif(option == float(6)):
                        result = input1 * 2.54
                        resultFunction(result)
                    
                    #km->sm
                    elif(option == float(7)):
                        result = input1 / 1.852
                        resultFunction(result)
                    
                    #sm->km
                    elif(option == float(8)):
                        result = input1 * 1.852
                        resultFunction(result)
                    
                distancesMenu(option)
            
            #volume
            elif(option == float (2)):
                result = "error: function not availible yet"
                resultFunction(result)

        conversionMenu(option)
    
    #space for more
    elif(option == float(5)):
        result = "error: function not availible yet"
        resultFunction(result)

    if(option == 0): 
        exit()

mainMenu()
