
#Playstation stock
#-- Estimate of how long a ps stock will last in a hipotetical relase of the console, 
#considering the work days on branches togheter with the range of failures on consoles 
# devuelta para regresar el stock uno mas
import random

stockps = 500
dayspassed = 0
opendays = {'m': True, 't': True, 'tu': True, 'w': True, 'th': False, 'f': True, 's': False, 'su': False}

while stockps > 0:
   
    for day in opendays.values():
       
         
         if day == True:
            if stockps > 40 and stockps < 60:
              sell = stockps
              stockps -= sell

             
              
              
            else:
              sell = random.randint(13, 20)
              stockps -= sell
            dayspassed += 1
                
            print(f"""Todays sellign has being: {str(sell)}
                      Stock to close of day: {str(stockps)}
                      days passed : {dayspassed}""")

            if stockps == 0 :
                 print(f"Sell ended with {dayspassed} days")
                 break
            
         else:
             dayspassed += 1
             print("DayOFF")
             print(f"days passed : {dayspassed}")


             
#El problema fue el while, con el loop, Es decir cuando pasa el while se ejecuta 7 veces
# Y es por eso que pasa a numeros negativos