import random

e = random.randint(0, 1)
while True: 
    manches = int(input("Combien de manches pour le BO ? "))
    assert manches%2 != 0, "Un BO se joue avec un nombre de manches impaires frère"
    match manches:
        case 1:
            if e == 0:
                print("On joue bande de pétasses")
            else:
                print("Go dormir bande de pétasses")
            break
        case _:
            dormir = 0
            jouer = 0
            for i in range(manches):
                essai = random.randint(0, 1)
                if essai == 0:
                    jouer += 1
                else:
                    dormir += 1
            if jouer > dormir:
                print(f"\n\n-------------------------------------------\n\tJouer : {jouer} - Dormir : {dormir} \n\tOn joue bande de pétasses\n-------------------------------------------\n")
            else:
                print(f"\n\n-------------------------------------------\n\tDormir : {dormir} - Jouer : {jouer} \n\tGo dormir bande de pétasses\n-------------------------------------------\n")
            break
    
