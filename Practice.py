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



student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_scores["Abraham"] = 99

student_grades = {}     

for student in student_scores:
      
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
         student_grades[student]  = "Exceeds Expectations"
    elif student_scores[student] > 70:
         student_grades[student] = "Acceptable" 
    else:
      student_grades[student] = "Fail"     

print(student_grades)   


#******----------------------------------------


Mexico = {
     "Puebla": ["Cuetzalan" , "Xicotepec" , "Tehuacan"], 
     "Guerrero" : ["San nicolas" , "Patzcuaro"]
} 


print(Mexico["Puebla"][1])

#-----------------------
def is_leap_year(year):
      if year % 400 == 0:
          return True
      elif year % 100 == 0:
          return False
      elif year % 4 == 0:
          return True
      else:
          return False
 
   