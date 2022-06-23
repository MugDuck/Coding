import random

from pyparsing import And
def main():{
    gameStart()
}
def gameStart():
    scoresum = 300
    randdiff = 10
    print("Hello player!")
    playerName = str(input("Please enter your username to begin: "))
    print(f"Alright, {playerName} lets begin.")
    gamePlay(playerName, scoresum, randdiff)

def gamePlay(name, score, randdiff):
    scoresum = score
    number = random.randint(1,randdiff)
    print(f"The number is {number}.")
    hiloinput = input(f"Okay {name}. Higher or lower? (type h or l:)  ").capitalize()
    newnumber = random.randint(1,10)
    #i get an error when i type anything other than h or l
    while hiloinput != "H" or hiloinput != "L":    
        if hiloinput == "H" and number >= newnumber:
            print("You selected higher.")
            print(f"The number was {newnumber} yours was higher!")
            print()
            randdiff = randdiff + 1
            scoresum = scoresum + 100
            print(f"Current Score: {scoresum}")
            gamePlay(name, scoresum, randdiff)
        elif hiloinput == "H" and number <= newnumber:
            print("You selected higher.")
            print(f"The number was {newnumber}, too bad yours was lower!")
            print()
            scoresum = scoresum - 75
            print(f"Current Score: {scoresum}")
            gamePlay(name, scoresum, randdiff)
        elif hiloinput == "L" and number <= newnumber:
            print("You selected lower.")
            print(f"The number was {newnumber}, yours was lower!")
            print()
            randdiff = randdiff + 1
            scoresum = scoresum + 100
            print(f"Current Score: {scoresum}")
            gamePlay(name, scoresum, randdiff)
        elif hiloinput == "L" and number >= newnumber:
            print("You selected lower.")
            print(f"The number was {newnumber}, too bad yours was higher!")
            print()
            scoresum = scoresum - 75
            print(f"Current Score: {scoresum}")
            gamePlay(name, scoresum, randdiff)
        

            
            
        elif hiloinput == "L" and number <= newnumber:
            print("You selected lower.")
            print(f"The number was {newnumber}, too bad yours was higher!")
            print()
            scoresum = scoresum - 75
            gamePlay(name, scoresum)
    
def tryagain():
    answer = input("Want to try again? y/n").capitalize()
    while answer != "Y" or answer != "N":
        if answer == "Y":
            print()
            gameStart()
        elif answer == "N":
            print()
            print("Thanks for playing!")
            exit()


    



main()
