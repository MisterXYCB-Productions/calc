def resultFunction(result, calculation):

    if(calculation):
        print(calculation)

    print("Das Ergebnis ist " + str(result))
    input1 = input("\n\n\nWenn du ins Hauptmenü zurück möchtest drücke \"y\"!")
    
    if(str(input1).lower() == "y"):
        return True
    else: 
        return False
