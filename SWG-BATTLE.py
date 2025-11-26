# HERE IS THE SNAKE-WATER-GUN GAME WITH HELP OF PYTHON CODE-->

import random

computer = random.choice([-1, 0, 1])

youDict = {"s": 1, "w": -1, "g": 0} # s: Snake (1), w: Water (-1), g: Gun (0)
reverseDict = {1: "snake", -1: "water", 0: "gun"}

youstr = input("Enter your choice (s for snake, w for water, g for gun):-").lower()

if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you].capitalize()}\nComputer chose {reverseDict[computer].capitalize()}")

    if computer == you:
        print("Its a draw!")

    elif (computer == -1 and you == 1): # Water vs Snake
        print("You win! (Snake drinks Water)")

    elif (computer == -1 and you == 0): # Water vs Gun
        print("You lose! (Gun sinks in Water)")

    elif (computer == 1 and you == -1): # Snake vs Water
        print("You lose! (Water drinks Snake)")

    elif (computer == 1 and you == 0): # Snake vs Gun
        print("You win! (Gun shoots Snake)")
        
    elif (computer == 0 and you == -1): # Gun vs Water
        print("You win! (Water sinks Gun)")
        
    elif (computer == 0 and you == 1): # Gun vs Snake
        print("You lose! (Snake shoots Gun)")