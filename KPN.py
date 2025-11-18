import random


SCORE = 0
while(True):
    x = random.randint(0,2)


    opcje = ["kamień", "papier", "nożyce"]

    komputer = opcje[x] # wybór komputera

    wybor = input("co wyrzucasz? [kamień, papier, nożyce]: ")
    
    wybor_lower = wybor.lower()

    if wybor_lower == komputer:
        print(F"remis")
        continue
    elif wybor_lower == "kamień" and komputer == "papier":
        print(F"przegrana! you stupid nygga straciłeś {SCORE} punkty")
    elif wybor_lower == "papier" and komputer == "nożyce":
        print(F"przegrana! you stupid nygga straciłeś {SCORE} punktow")
    elif wybor_lower == "nożyce" and komputer == "kamień":
        SCORE = 0
        print(F"przegrana! you stupid nygga straciłeś {SCORE} punktow")
    else:
        SCORE += 1
        print(F"wygrałeś! zyskujesz {SCORE}  punkty.")
        
    