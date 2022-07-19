import random
flexing = input("On prend en compte les games en Flex ? (o/n) ")
manches = int(input("Combien de manches pour le BO ? "))
assert manches%2 != 0, "Un BO se joue avec un nombre de manches impaire sans s frère"

if flexing == "o":
    match manches:
        case 1:
            e = random.randint(0, 2)
            if e == 0:
                print(f"\n\n---------------------------------------------------\n\t Jouer : 1 - Dormir : 0 - Flex : 0 \n\t   On joue bande de pétasses\n---------------------------------------------------\n")
            elif e == 1:
                print(f"\n\n---------------------------------------------------\n\t Dormir : 1 - Jouer : 0 - Flex : 0\n\t   Go dormir bande de pétasses\n---------------------------------------------------\n")
            else:
                print(f"\n\n---------------------------------------------------\n\t Flex : 1 -Jouer : 0 - Dormir : 0 \n\t   Go flex bande de pétasses\n---------------------------------------------------\n")
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
                elif essai == 1:
                    dormir += 1
                else:
                    flex += 1
            if jouer == flex == dormir:
                e = random.randint(0, 2)
                if e == 0:
                    print(f"\n\n---------------------------------------------------\n\t Jouer : 1 - Dormir : 0 - Flex : 0 \n\t   On joue bande de pétasses\n---------------------------------------------------\n")
                elif e == 1:
                    print(f"\n\n---------------------------------------------------\n\t Dormir : 1 - Jouer : 0 - Flex : 0\n\t   Go dormir bande de pétasses\n---------------------------------------------------\n")
                elif e == 2:
                    print(f"\n\n---------------------------------------------------\n\t Flex : 1 -Jouer : 0 - Dormir : 0 \n\t   Go flex bande de pétasses\n---------------------------------------------------\n")
            elif jouer == dormir and (flex < jouer and flex < dormir): #tg cédric
                print("Egalité entre jouer et dormir avec une valeur de", dormir)
                e = random.randint(0, 1)
                if e == 0:
                    print(f"\n\n---------------------------------------------------\n\t Jouer : 1 - Dormir : 0 - Flex : 0 \n\t   On joue bande de pétasses\n---------------------------------------------------\n")
                else:
                    print(f"\n\n---------------------------------------------------\n\t Dormir : 1 - Jouer : 0 - Flex : 0\n\t   Go dormir bande de pétasses\n---------------------------------------------------\n")
            elif flex == dormir and (jouer < flex and jouer < dormir):
                print("Egalité entre flex et dormir avec une valeur de", dormir)
                e = random.randint(0, 1)
                if e == 0:
                    print(f"\n\n---------------------------------------------------\n\t Flex : 1 - Jouer : 0 - Dormir : 0\n\t   Go flex bande de pétasses\n---------------------------------------------------\n")
                else:
                    print(f"\n\n---------------------------------------------------\n\t Dormir : 1 - Jouer : 0 - Flex : 0\n\t   Go dormir bande de pétasses\n---------------------------------------------------\n")
            elif flex == jouer and (dormir < flex and dormir < jouer):
                print("Egalité entre flex et jouer avec une valeur de", jouer)
                e = random.randint(0, 1)
                if e == 0:
                    print(f"\n\n---------------------------------------------------\n\t Jouer : 1 - Dormir : 0 - Flex : 0 \n\t   On joue bande de pétasses\n---------------------------------------------------\n")
                else:
                    print(f"\n\n---------------------------------------------------\n\t Flex : 1 -Jouer : 0 - Dormir : 0 \n\t   Go flex bande de pétasses\n---------------------------------------------------\n")
            else:
                if max(jouer, dormir, flex) == jouer:
                    print(f"\n\n---------------------------------------------------\n\t Jouer : {jouer} - Dormir : {dormir} - Flex : {flex}\n\t   On joue bande de pétasses\n---------------------------------------------------\n")
                elif max(jouer, dormir, flex) == dormir:
                    print(f"\n\n---------------------------------------------------\n\t Dormir : {dormir} - Jouer : {jouer} - Flex : {flex}\n\t   Go dormir bande de pétasses\n---------------------------------------------------\n")
                else:
                    print(f"\n\n---------------------------------------------------\n\t Flex : {flex} - Jouer : {jouer} - Dormir : {dormir}\n\t   Go flex bande de pétasses\n---------------------------------------------------\n")
else :
    e = random.randint(0, 1)
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
