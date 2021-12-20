#Famille1 = dict(Maxence=20, Adeline = 22, Monique = 50, Stephane = 51, Loriane = 16)
class Personne:
    def __init__(self, nom, prenom, age, sexe, travail, loisirs):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.travail = travail
        self.loisirs = loisirs
    
class Famille:
    def __init__(self, FamilyName, nb_membres, NomsMembres, ages, FamilleFinale):
        self.name = FamilyName
        self.nombre_membres = nb_membres
        self.NomsMembres = NomsMembres
        self.ages = ages
        self.FamilleFinale = FamilleFinale #un dictionnaire contenant {Key = Noms : Value = Âge}


class Membre(Personne):
    def __init__(self, lerap):
        super()
        user = input("Voulez vous rejoindre une famille ?\n")
        print(user)
        if (user != "Oui" or "O" or "o"):
            self.famille = CreationFamille()
        else:
            self.famille = RejoindreFamille()

    def QuitterLaFamille(self, ):
        self.famille = Famille('', 0, '', '', dict())

    def NouvelleFamille(self):
        RejoindreFamille()

def RejoindreFamille():
    print("debug")

def CreationFamille():
    FamilyName = input("Veuillez entrer votre nom de famille : \n")
    Nb_Members = int(input("Veuillez entrer le nombre de membres de votre famille :\n"))
    NomsMembres = [] 
    FamilleFinale = dict()
    Noms_Ages_J = dict()
    age = []
    i = 0
    j = 0

    while (len(NomsMembres) < 2):
        noms = input(f"Veuillez entrer le noms des deux parents de votre famille :\nParent {len(NomsMembres) + 1} : ")
        NomsMembres.append(noms)  

    while i < 2:
        AgeInput = int(input(f"Veuillez entrer l'âge de {NomsMembres[i]} :\n"))
        age.append(AgeInput)
        i += 1

    while (len(NomsMembres) < Nb_Members):
        noms = input(f"Veuillez entrer le noms des enfants de votre famille :\nEnfant {len(NomsMembres) - 1} : ")
        NomsMembres.append(noms)  

    while (len(age) < Nb_Members):
        AgeInput = int(input(f"Veuillez entrer l'âge de {NomsMembres[i]} :\n"))
        age.append(AgeInput)
        i += 1

    
    print(f"La famille {FamilyName} comptant {Nb_Members} membres s'appellant {NomsMembres} a bien été ajoutée dans notre base de donnée.\n\n")

    while j<len(age):
        print(f"{NomsMembres[j]} a {age[j]} ans\n")
    
        #Noms_Ages_J = {NomsMembres[j] : age[j]}
        FamilleFinale.update({NomsMembres[j] : age[j]})

        j += 1
    
    
    FamilleFinale.update(dict(sorted(FamilleFinale.items(), key=lambda item: item[1])))
    Fam = Famille(FamilyName, Nb_Members, NomsMembres, age, FamilleFinale)
    print(f"\n\n\n La famille finale est donc {FamilleFinale}")

    return Fam

Maxence = Personne('Blazy', 'Maxence', 20, 'Homme', 'Etudiant', 'Jeux vidéos')
Blazouille = Membre(Maxence)

# FamFin =  {'Stephane' : 50, 'Monique' : 49, 'Loriane' : 16, 'Adeline' : 23, 'Maxence' : 20}
# for w in sorted(FamFin, key=FamFin.get, reverse=True):
#     FamFin.update(dict(w = FamFin[w]))
# #A voir comment faire, Loriane se transforme en w wtf frr

# Fam = Famille('Blazy', 5, ['Stephane', 'Monique', 'Loriane', 'Adeline', 'Maxence'], [50, 49, 16, 22, 20], FamFin)
# #print(Fam.FamilleFinale)

