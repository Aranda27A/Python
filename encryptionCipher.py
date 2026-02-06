import string
alphabet =list(string.ascii_lowercase)


def encrypth(originaltext , shiftNumber):
    Textcoded = ""
    for char in originaltext:
       
        if char == " ":
            Textcoded+= " "
        else:
            shiftposition = alphabet.index(char) + shiftNumber
            shiftposition %= len(alphabet)
            Textcoded+= alphabet[shiftposition]
       
    print(f"here is the encoded text: {Textcoded}") 




def dencrypt(originaltext , shiftNumber):
    textUncoded = ""
    for char in originaltext:
          if char == " ":
            textUncoded+= " "
          else:
            shiftposition = alphabet.index(char) - shiftNumber
            shiftposition %= len(alphabet)
            textUncoded += alphabet[shiftposition] 
    print(f"Here you got you decoded text: {textUncoded}")


        

def menu():
    action = input("What would you like to do: write: 'code' to encode or 'decode' to decrypt.\n")
    text = input("Insert text to encoden/decode:\n").lower()
    shiftnum = int(input("Locate the number to shift\n "))


    if action == "code":
        encrypth(text, shiftnum)
    elif action == "decode":
        dencrypt(text, shiftnum)  



menu()
 