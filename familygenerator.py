from Fun import Famille
import random as r

liste_de_prenom = ['Martin', 'Bernard', 'Thomas', 'Henri', 'Cedric', 'Léo', 'Léonard', 'Maxime', \
        'Néo', 'Nathan', 'Stephane', 'Romain', 'Samuel', 'Monique', 'Adeline', 'Loriane', 'Alice', 'Mikaela', \
            'Myriam', 'Léa', 'Marie', 'Manon', 'Hanna', 'Irma', 'Jusefs', 'Jacques', 'François', 'Yann', \
                'Marc', 'Yassine'] 

#25 Prénoms
#print("\n\n", liste_de_prenom,"\n\n")

liste_de_nom = ['Blazy', 'Bonhomme', 'Atiyeh', 'Brault', 'Pineda', 'Brousse', 'Béal', 'Taussat', 'Saade', 'Portecop']

#10 Familles
#print(liste_de_nom,"\n\n")

liste_age = [ r.randint(10, 50) for _ in range(30) ]

#25 ages
#print("\n\n",liste_age)

liste_nb_membres = [3 for _ in range(10)]
#3 membres pour les 10 familles

def GenerateTenFamilies(liste_de_prenom, liste_de_nom, liste_age, liste_nb_membres):

    assert len(liste_de_nom) == 10 , f"""Veuillez entrer une liste de nom de taille 10 ; la taille actuelle est de \
{len(liste_de_nom)}"""

    liste_de_famille = []

    for _ in range(10):
        x = liste_de_nom[_]
        prenoms = list()
        age = list()
        i = 0
        j = 0
        k = 0
        FamFin = dict()

        #marche avec 30 prénoms seulement et 3 personnes par famille !

        while (i != 3):
            rndom1 = r.randint(0, len(liste_de_prenom)-1)
            prenoms.append(liste_de_prenom[rndom1])
            liste_de_prenom.remove(liste_de_prenom[rndom1])
            i += 1

        while (j != 3):
            rndom2 = r.randint(0, len(liste_age)-1)
            age.append(liste_age[rndom2])
            liste_age.remove(liste_age[rndom2])
            j += 1

        while (k < 3):
            FamFin.update({prenoms[k] : age[k]})
            k += 1

        fam = Famille(str(x), liste_nb_membres[_], prenoms, age, FamFin) 
        print(f"\nFamille {_+1}: {FamFin}")
        liste_de_famille.append(fam) 

GenerateTenFamilies(liste_de_prenom, liste_de_nom, liste_age, liste_nb_membres)