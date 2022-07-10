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

class Membre(Personne):
    def __init__(self):
        super().__init__

        user = input("Voulez vous créer une famille ?\n")
        oui = ['Oui', 'o', 'oui', 'O']
        print(user)

        if (user in oui):
            self.famille = CreationFamille()
        else:
            self.famille = RejoindreFamille()

    def QuitterLaFamille(self, ):
        self.famille = Famille('', 0, '', '', dict())

    def NouvelleFamille(self):
        RejoindreFamille()

Maxence = Personne('Blazy', 'Maxence', 20, 'Homme', 'Etudiant', 'Jeux Vidéos')


"""
mettre les familles dans un fichier texte comme base de donnée ; chaque famille aura un fichier texte avec toutes les infos dedans
"""