import random as r

from Fun import Famille

from time import sleep

itérations = int(0)

def GenerateTenFamilies(itérations):

    while itérations < 3:

        liste_de_prenom = ['Martin', 'Bernard', 'Thomas', 'Guillaume', 'Cedric', 'Léo', 'Léonard', 'Maxime', \
        'Néo', 'Nathan', 'Stephane', 'Romain', 'Samuel', 'Monique', 'Adeline', 'Loriane', 'Alice', 'Jett', \
            'Melanie', 'Léa', 'Marie', 'Manon', 'Hanna', 'Sonia', 'Jusefs', 'Jacques', 'François', 'Yann', \
                'Marc', 'Yassine'] 
        #25 Prénoms
        #print("\n\n", liste_de_prenom,"\n\n")

        liste_de_nom = ['Blazy', 'Bonhomme', 'Atiyeh', 'Davy', 'Lfigp', 'Adarif', 'Béal', 'Taussat', 'Saade', 'Portecop']

        #10 Familles
        #print(liste_de_nom,"\n\n")

        liste_age = [ r.randint(10, 50) for _ in range(30) ]

        #25 ages
        #print("\n\n",liste_age)

        liste_nb_membres = [3 for _ in range(10)]
        #3 membres pour les 10 familles
        liste_de_famille = []
        
        assert len(liste_de_nom) == 10, \
        f"""Veuillez entrer une liste de nom de taille 10 ; la taille actuelle est de {len(liste_de_nom)}"""
        
        count = itérations+1 if itérations != 0 else ""
        with open(f"bddFam/bdd{count}.md", "w") as data:
            for _ in range(10):
                x = liste_de_nom[_]
                prenoms = list()
                age = list()
                i = 0
                k = 0
                FamFin = dict()

                #marche avec 30 prénoms seulement et 3 personnes par famille !

                while (i != 3):
                    rndom1 = r.randint(0, len(liste_de_prenom)-1)
                    prenoms.append(liste_de_prenom[rndom1])
                    liste_de_prenom.remove(liste_de_prenom[rndom1])
                    rndom2 = r.randint(0, len(liste_age)-1)
                    age.append(liste_age[rndom2])
                    liste_age.remove(liste_age[rndom2])
                    i += 1

                while (k < 3):
                    FamFin.update({prenoms[k] : age[k]})
                    k += 1

                #trie en fonction de l'âge    
                """on prend toutes les valeurs, on les fout dans une liste qu'on sort, et on update le dictionnaire avec """
                dictFam = []
                
                for w in sorted(FamFin, key=FamFin.get, reverse=True):
                    FamFin.update(dict(w = FamFin[w]))
                del(FamFin['w'])

                fam = Famille(str(x), liste_nb_membres[_], prenoms, age, FamFin) 
                data.write(f"Famille {liste_de_nom[_]}\n{FamFin}\n\n")
                liste_de_famille.append(fam) 
        itérations += 1
        # sleep(5)
GenerateTenFamilies(itérations)