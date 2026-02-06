def calculate_love_score(name1, name2):
    Check1 = ["t","r","u","e"]
    Check2 = ["l","o","v","e"]
    names = name1 + name2
    scoretrue = 0
    scorelove = 0

    for char in names:
     if char in Check1:
        scoretrue += 1
     if char in Check2:
        scorelove += 1 

    print(f"{scoretrue}{scorelove}")
    print(names)
    

calculate_love_score("Kanye West" , "Kim Kardashian")