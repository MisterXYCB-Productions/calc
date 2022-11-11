import random

def rps():
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
            print("\nTie! We both chose rock!\n")
        if user_choice == computer_choice and user_choice == 2:
            print("\nTie! We both chose paper!\n")
        if user_choice == computer_choice and user_choice == 3:
            print("\nTie! We both chose scissors!\n")
        elif user_choice == 1 and computer_choice == 2:
            print("\nYou lose! I chose paper and you rock!\n")
        elif user_choice == 1 and computer_choice == 3:
            print("\nYou win! You chose rock and i scissors!\n")
        elif user_choice == 2 and computer_choice == 1:
            print("\nYou win! You chose paper and i rock!\n")
        elif user_choice == 2 and computer_choice == 3:
            print("\nYou lose! I chose scissors and you paper!\n")
        elif user_choice == 3 and computer_choice == 1:
            print("\nYou lose! I chose rock and you scissors!\n")
        elif user_choice == 3 and computer_choice == 2:
            print("\nYou win! You chose scissors and i paper!\n")
        elif(user_choice == float(69)):
            print("\nNice!\n")
        else:
            print("\nYou loose because you didnt choose anything\n")
        print("Please choose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        user_choice = int(input("Enter your choice: "))
    print("Thanks for playing")
    return