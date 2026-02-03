import random

Ticketsnumber = random.randint(1 , 100)

if Ticketsnumber % 2 == 0 and not Ticketsnumber % 12 == 0:
    print(f"Yo are look one\n{Ticketsnumber}")
    
     
elif Ticketsnumber % 4 == 0 and Ticketsnumber % 3 == 0:
    print("You have a secret numer, just 8 people has it") 
         
    if Ticketsnumber == 12:
            print("12, has ganado un million")
    elif Ticketsnumber == 24:
            print("24, has ganado un pete ")
    else: print(f"reclama tu premio,  {Ticketsnumber}")




else: print("continue")




#----------------------------------------------



for numero in range(1,100):  
     if  numero % 3 == 0 and numero % 5 == 0 :
           
           print("FIZZBUZZ ")
     elif numero % 3 == 0:
           print("FIZZ")
     elif numero % 5 == 0:
           print("BUZZ")
     else:
           print(f"{numero}")


#Error in logic, but works


#--------------------------------------------------------

import string


abece = string.ascii_letters
pasword = []

for char in  range(1, random.randint(6,10)):
 pasword.append(random.choice(abece))

for num in range(4,10):
     pasword.append(str(int(random.random()*10)))


print(pasword)

password = ""
for char in pasword:
     password += char

print(password)

#--------------------------------------------------------



#******----------------------------------------

    


