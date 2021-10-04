import random
import time
print("Welcome to squid game #5")
print("The rules are simple")
print("There are 16 players, 1 being you")
print("Player order will randomly be decided")
print("Players will go in order to get through 20 glass panels")
print("There are two sides of glass panels")
print("The left side, we will call 0 in this case, and the right side which we will call 1")
print("One side will be weak glass that will cause you to fall to your death")
print("While the other side is strong glass allowing you to make it to the next tile")
print()
while True:
    checker = input("Are you ready to play? Type y/Y if not type anything else: ")
    if checker == 'y' or checker =='Y':
        x = random.randint(1,16)
        print()
        print("YOU ARE NUMBER: " + str(x))
        print()

        #for loop to determine the board of tiles
        board = []
        for i in range(20):
            board.append(random.randint(0,1))
        
        tileNumber = 0
        for i in range(x - 1): #the people in front leading the way
            alive = True
            while alive and tileNumber < 20:
                choice = random.randint(0,1)
                if choice == board[tileNumber]:
                    print("player " + str(i + 1) + " has cleared tile #" + str(tileNumber + 1))
                    print()
                    time.sleep(.75)
                    tileNumber = tileNumber + 1
                else:
                    print("Player " + str(i + 1) + " has died on tile #" + str(tileNumber + 1))
                    print()
                    tileNumber = tileNumber + 1
                    time.sleep(.75)
                    alive = False
        if tileNumber == 20:
            print("You have made it across alive!")
            print()
            continue
        print("You are at tile #" + str(tileNumber + 1) + "!")
        
        alive = True
        while alive and tileNumber < 20:
            choice = input("Please choose a glass tile by typing 0 or 1: ")
            if int(choice) == board[tileNumber]:
                print()
                print("You made the correct choice!")
                print("you are now on tile #" + str(tileNumber + 1))
                print()
                tileNumber = tileNumber + 1
            else:
                print()
                print("YOU FELL TO YOUR DEATH!")
                print()
                alive = False
        if tileNumber == 20:
            print("Congratulations you have beat the game!")
        continue
    else:
        break




