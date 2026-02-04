#Hangman 
import random

word = ["abraham" ,"solaris" ,"jueputa"]

chooseWord = random.choice(word)
print(chooseWord)
sizeLetter = len(chooseWord)
userchart = ""

for space in range(sizeLetter):
     userchart += "_"
print(userchart)  


gameOver = False
Guessletter = []
life = 3

while not gameOver:
    display = ""
    userSelection = input("Guess the char of the letter: ").lower()

    if userSelection in Guessletter:
          life-=1
          print(f"You lost a life, you have {life} left")
          if life == 0:
                print("You have no life left")
                gameOver = True
                
    
    for char in chooseWord:

        if  userSelection == char:
            display += char
            Guessletter.append(userSelection)

        elif char in Guessletter:
                 display += char
        else: 
                 display += "_"
                 
    if userSelection not in chooseWord :
            life -= 1
            if life == 0:
                print("You have no life left")
                gameOver = True
            print(f"You lost a life, you have {life} left")
   
    if "_" not in display:
            gameOver = True
            print("You WIN")

    print(display)
          