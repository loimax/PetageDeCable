import os
import time
path = os.path.abspath(__file__) #get path without file name
class Personne:
    def __init__(self, nom, prenom, age, sexe, travail, loisirs):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.travail = travail
        self.loisirs = loisirs
  
class Famille:
    def __init__(self, *args):
        if len(args) == 5:
            self.name = args[0]
            self.nombre_membres = args[1]
            self.NomsMembres = args[2]
            self.ages = args[3]
            self.FamilleFinale = args[4] #un dictionnaire contenant {Key = Noms : Value = Âge}
        elif len(args) == 2: #full path to bdd and number of families to create from it
            self.liste_famille = []
            iter = args[1]
            for _ in range(iter):
                count = _
                with open(f"{args[0]}", "r") as data:
                    for line in data:
                        if line.startswith("F"):
                            if count > 0:
                                count -= 1
                            else:
                                ligne=line[8:-1]
                                self.name = list()
                                self.name.append(ligne)
                                # print(self.name)
                                break
                count = _
                with open(f"{args[0]}", "r") as data:
                    for line in data:
                        if line.__contains__("{"):
                            if count > 0:
                                count -= 1
                            else:
                                ligne = line.split("{")[1].split("}")[0]
                                self.NomsMembres = list()
                                while(len(ligne)>4):
                                    if ligne.__contains__("'"):
                                        nom = ligne.split("'")[1].split("'")[0]
                                        self.NomsMembres.append(nom)
                                        count = len(ligne.split(":")[1].split("'")[0])+1
                                        ligne = ligne[len(nom)+2+count:]
                                    else:
                                        break
                                # print(self.NomsMembres)
                                break
                count = _
                with open(f"{args[0]}", "r") as data:
                    for line in data:
                        if line.__contains__("{"):
                            if count > 0:
                                count -= 1
                            else:
                                ligne = line.split("{")[1].split("}")[0]
                                self.ages = list()
                                while(len(ligne)>4):
                                    if ligne.__contains__(":"):
                                        age = ligne.split(":")[1].split(",")[0][1:]
                                        self.ages.append(age)
                                        if ligne.split(":")[1].count(",") > 0:
                                            count = len(ligne.split("'")[1].split(",")[0])+ len(age) + 6
                                        ligne = ligne[count:]
                                    else:
                                        break
                                break

                self.nombre_membres=len(self.NomsMembres)
                self.FamilleFinale = dict(zip(self.NomsMembres, self.ages))
                fam = Famille(self.name, self.nombre_membres, self.NomsMembres, self.ages, self.FamilleFinale)
                self.liste_famille.append(fam)

            with open(f"{os.path.dirname(path)}/bddFam/bddFunListe.md", "a") as data:
                data.write(f"--------------------------------------\n")
                for i in self.liste_famille:
                    data.write(f"\t\t\t{i.FamilleFinale}\n")
                data.write(f"--------------------------------------\n")

        else:
            FamilyName = input("Veuillez entrer votre nom de famille : \n")
            Nb_Members = int(input("Veuillez entrer le nombre de membres de votre famille :\n"))
            NomsMembres = [] 
            FamilleFinale = dict()
            age = []
            i = 0
            j = 0

            print("Veuillez entrer les noms du/des parent/parents:")
            while len(NomsMembres) < 2:
                noms = input(f"Parent {len(NomsMembres) + 1} : ")
                NomsMembres.append(noms)
                if len(NomsMembres) == 2:
                    break
                elif input("Voulez-vous ajouter un autre parent ? (O/N) : ") == "O":
                    continue
                else:
                    break

            while i < len(NomsMembres):
                AgeInput = int(input(f"Veuillez entrer l'âge de {NomsMembres[i]} :\n"))
                age.append(AgeInput)
                i += 1

            countx=1
            print("\nVeuillez entrer le noms des enfants de votre famille :")
            while (len(NomsMembres) < Nb_Members):
                
                noms = input(f"Enfant {countx} : ")
                NomsMembres.append(noms)  
                countx += 1

            print("")
            while (len(age) < Nb_Members):
                AgeInput = int(input(f"Veuillez entrer l'âge de {NomsMembres[i]} :\n"))
                age.append(AgeInput)
                i += 1
            # print(f"La famille {FamilyName} comptant {Nb_Members} membres s'appellant {', '.join(NomsMembres)} a bien été ajoutée dans notre base de donnée.\n\n")

            while j<len(age):
                FamilleFinale.update({NomsMembres[j] : age[j]})
                j += 1

            FamilleFinale = dict(sorted(FamilleFinale.items(), key=lambda item: item[1], reverse = True))
            print(f"\n\n\nLa famille finale est donc {FamilleFinale}")
            
            age.sort(reverse = True)
            self.name = FamilyName
            self.nombre_membres = Nb_Members
            self.NomsMembres = NomsMembres
            self.ages = age
            self.FamilleFinale = FamilleFinale

    def setName(self, name):
        self.name = name
    def setNbMembres(self, nb_membres):
        self.nombre_membres = nb_membres
    def setNomsMembres(self, NomsMembres):
        self.NomsMembres = NomsMembres
    def setAges(self, ages):
        self.ages = ages
    def getName(self):
        return self.name
    def getNbMembres(self):
        return self.nombre_membres
    def getNomsMembres(self):
        return self.NomsMembres
    def getAges(self):
        return self.ages

    def toBdd(self):
        with open(f"{os.path.dirname(path)}/bddFam/bddFun.md", "a") as data:
            data.write(f"--------------------------------------\n")
            data.write(f"\t\t\tFamille {self.name}\n")
            data.write(f"--------------------------------------\n")
            for _ in self.FamilleFinale.keys():
                data.write(f"\t{_} est agé(e) de {self.FamilleFinale.get(_)} an(s)\n")
                   
while 1:
    choice = int(input("""\n
    Voulez-vous :\n\t
    1. Ajouter une famille\n\t
    2. Afficher la base de donnée\n\t
    3. Générer plusieurs familles aléatoirement\n\t
    4. Afficher la base de donnée des familles générées\n\t
    5. Supprimer la base de donnée des familles générées\n\t
    6. Quitter\n"""))
    match choice:
        case 1:
            fam = Famille()
            fam.toBdd()
        case 2:
            with open(f"{os.path.dirname(path)}/bddFam/bddFun.md", "r") as data:
                print(data.read())
        case 3:
            nb_fam = int(input("Combien de familles voulez-vous générer ?\n"))
            os.system(f"python {os.path.dirname(path)}/familygenerator.py")
            Famille(f"{os.path.dirname(path)}/bddFam/bdd.md", nb_fam)
            os.remove(f"{os.path.dirname(path)}/bddFam/bdd.md")
            break
        case 4:
            with open(f"{os.path.dirname(path)}/bddFam/bddFunListe.md", "r") as data:
                print(data.read())
        case 5:
            os.remove(f"{os.path.dirname(path)}/bddFam/bddFunListe.md")
        case 6:
            break
