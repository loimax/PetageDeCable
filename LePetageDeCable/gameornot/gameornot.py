import random
e = random.randint(0, 1)
manches = int(input("Combien de manches pour le BO ? "))
assert manches%2 != 0, "Un BO se joue avec un nombre de manches impaire sans s frère"
match manches:
    case 1:
        if e == 0:
            print(f"\n\n-------------------------------------------\n\t Jouer : 1 - Dormir : 0 \n\tOn joue bande de pétasses\n-------------------------------------------\n")
        else:
            print(f"\n\n-------------------------------------------\n\t Dormir : 1 - Jouer : 0 \n\tGo dormir bande de pétasses\n-------------------------------------------\n")
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
        if jouer > dormir:
            print(f"\n\n-------------------------------------------\n\t Jouer : {jouer} - Dormir : {dormir} \n\tOn joue bande de pétasses\n-------------------------------------------\n")
        else:
            print(f"\n\n-------------------------------------------\n\t Dormir : {dormir} - Jouer : {jouer} \n\tGo dormir bande de pétasses\n-------------------------------------------\n")

