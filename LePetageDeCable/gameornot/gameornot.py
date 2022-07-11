from decimal import Decimal
import random

e = random.randint(0, 1)
manches = int(input("Combien de manches pour le BO ? "))
assert manches%2 != 0, "Un BO se joue avec un nombre de manches impaires frère"
match manches:
    case 1:
        if e == 0:
            print("On joue bande de pétasses")
        else:
            print("Go dormir bande de pétasses")
    case _:
        dormir = 0
        jouer = 0
        for i in range(manches):
            essai = random.randint(0, 1)
            if jouer >= (manches / 2) or dormir >= abs(manches / 2):
                break
            if essai == 0:
                jouer += 1
            else:
                dormir += 1
            # print("Jouer =", jouer, " Dormir = ", dormir)
        if jouer > dormir:
            print(f"\n\n-------------------------------------------\n\t Jouer : {jouer} - Dormir : {dormir} \n\tOn joue bande de pétasses\n-------------------------------------------\n")
        else:
            print(f"\n\n-------------------------------------------\n\t Dormir : {dormir} - Jouer : {jouer} \n\tGo dormir bande de pétasses\n-------------------------------------------\n")

