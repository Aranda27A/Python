"""
Docstring for blackjack
Make a mini blackjack game with the following rules:
- The deck is unlimited in size. There are no jokers.
- The Jack/Queen/King all count as 10. The Ace can count as 11 or 1.
- Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
- Cards are not removed from the deck as they are drawn.
- The user is asked if they want to draw another card. If the user goes over 21, they lose.
- The dealer will draw cards until it has 17 or more. If the dealer goes over 21, the user wins.
- The winner is the player with the highest score under 22.


"""
import random


user_count = []
compu_count = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over = False


def deal_card():
 return random.choice(cards)

def calculateCards(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score
   
def blackjack():
   global is_game_over 

   
   for _ in range(2):  
    user_count.append(deal_card())
    compu_count.append(deal_card())

   while not is_game_over:
      scoreUser = calculateCards(user_count)
      scoreCompu = calculateCards(compu_count)

      print(f"Compu a obtenido {compu_count[0]} y tu usuario: {scoreUser} de score con {user_count}")

      if scoreUser > 21:
        is_game_over = True
        print("Has perdido usuario")
        break
      if scoreUser == 21:
        print("Perfect score")
        is_game_over = True
        break
       

      avanzar = input("Deseas tomar otra carta, selecciona 'y' para continuar ")

      if avanzar == "y":
       user_count.append(deal_card())
      else:
       is_game_over = True


   while calculateCards(compu_count) < 17:
        compu_count.append(deal_card())

   finalScore = calculateCards(user_count)
   Finalscorecompu = calculateCards(compu_count)

   print(f"Compu = {Finalscorecompu} con {compu_count} ny  tu {finalScore}")

   if finalScore > 21:
     print("Has perdido")
   elif finalScore > 21 or finalScore > Finalscorecompu:
    print("has ganado")
   elif Finalscorecompu > finalScore:
     print("has perdido")
   else:
     print("empate")

blackjack()