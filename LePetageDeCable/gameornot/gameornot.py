import random
e = random.randint(0, 2)
manches = int(input("Combien de manches pour le BO ? "))
assert manches%2 != 0, "Un BO se joue avec un nombre de manches impaire sans s frère"
match manches:
    case 1:
        if e == 0:
            print(f"\n\n---------------------------------------------------\n\t Jouer : 1 - Dormir : 0 - Flex : 0 \n\tOn joue bande de pétasses\n---------------------------------------------------\n")
        elif e == 1:
            print(f"\n\n---------------------------------------------------\n\t Dormir : 1 - Jouer : 0 - Flex : 0\n\tGo dormir bande de pétasses\n---------------------------------------------------\n")
        else:
            print(f"\n\n---------------------------------------------------\n\t Flex : 1 -Jouer : 0 - Dormir : 0 \n\tGo flex bande de pétasses\n---------------------------------------------------\n")
    case _:
        dormir = 0
        jouer = 0
        flex = 0
        for i in range(manches):
            essai = random.randint(0, 2)
            if jouer >= (manches / 2) or dormir >= (manches / 2) or flex >= (manches / 2):
                break
            if essai == 0:
                jouer += 1
            elif e == 1:
                dormir += 1
            else:
                flex += 1
        if max(jouer, dormir, flex) == jouer:
            print(f"\n\n---------------------------------------------------\n\t Jouer : {jouer} - Dormir : {dormir} - Flex : {flex}\n\tOn joue bande de pétasses\n---------------------------------------------------\n")
        elif max(jouer, dormir, flex) == dormir:
            print(f"\n\n---------------------------------------------------\n\t Dormir : {dormir} - Jouer : {jouer} - Flex : {flex}\n\tGo dormir bande de pétasses\n---------------------------------------------------\n")
        else:
            print(f"\n\n---------------------------------------------------\n\t Flex : {flex} - Jouer : {jouer} - Dormir : {dormir}\n\tGo flex bande de pétasses\n---------------------------------------------------\n")
