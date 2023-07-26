import random
Rock = 1
Paper = 2
Scissors = 3
name = input("Enter your name: ")
while True:
    computer = random.randint(1, 3)
    print("Welcme to Rock-Paper-Scissors-Shut: "+name)
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choose =int(input("Enter choice,(1, 2, 3): ")) 
    if choose == 1:
        if computer == 3:
            print(name+" Won")
        if computer == 2:
            print("Bot1 beat you")
        if computer == 1:
            print("Tie")
    if choose == 2:
        if computer == 1:
            print(name+" Won")
        if computer == 3:
            print("Bot1 beat you")
        if computer == 2:
            print("Tie")
    if choose == 3:
        if computer == 2:
            print(name+" Won")
        if computer == 1:
            print("Bot1 beat you")
        if computer == 3:
            print("Tie")
    question = input("Do you want to play again (y,n): ")
    if question == "n":
        break