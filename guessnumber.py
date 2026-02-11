import random
Lifes = 0
numToguess = random.randint(1, 100)


def chooseDifficultie() : 
    global Lifes 

    difficultie = input("Escoge la dificultad: 'easy' or 'hard' ")
    if difficultie == "easy":
        Lifes += 10
    elif difficultie == "hard":
        Lifes += 5
    else:
        print("Vuelve a intentralo")

    

def guessNumber(n):
    global Lifes

    chooseDifficultie()
  
    while Lifes > 0:
        chooseNumber = int(input("Elige un numero entre 1 a 100: "))

        if chooseNumber > n:
            print("Too far")
            Lifes -= 1
         
        elif chooseNumber < n:
            print("Too low")
            Lifes -= 1
         
        else:
            print("Correcto number")
            break
    if Lifes == 0:
        print("Cero vidas")
    

guessNumber(numToguess)