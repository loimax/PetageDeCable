from os import remove
import sys
import webbrowser
import time
list_players = []
list_referee = []
dict_rencontres = dict()
while True: 
#possibilité d'ajouter un menu avec while true pour avoir un menu en background et un menu de choix de l'utilisateur
    print("""
    1. Add Player
    2. Add Referee
    3. Show Players
    4. Show Referees
    5. Exit this menu
    6. Open Webpage
    """)
    choice = input("Enter your choice: ") #int(input("Enter your choice: "))
    match choice:
        case "1":
            name = input("Enter player name: ")
            list_players.append(name)
        case "2":
            name = input("Enter referee name: ")
            list_referee.append(name)
        case "3":
            print("Players: ")
            for i in list_players:
                print(i)
        case "4":
            print("Referees: ")
            for i in list_referee:
                print(i)
        case "5":
            break
        case "6":
            arbitre = list_referee
            date = input("Enter match full date: ")

            hs = open("convocation.html", 'w')

            strTable = f"<!DOCTYPE html><html><body><p>Nom de l'arbitre : {arbitre} </p><br/><h3>Liste des joueurs</h3>"
            for players in list_players:
                strRW = players + "<br>"
                strTable = strTable+strRW
            strTable = strTable+f"<h5>Heure de la rencontre : {date}<h5/>"
            strTable = strTable+"</body></html>"
            
            hs.write(strTable)
            hs.close()

            time.sleep(5)
            url = 'convocation.html'

            # Open URL in new tab if needed, or just open URL in a Safari window
            chrome_path = 'open -a /Applications/Safari.app %s'
            webbrowser.get(chrome_path).open(url)
            time.sleep(5)
            remove('convocation.html')
            sys.exit(0)
        case _:
            print("Invalid choice")

    # break
#https://www.youtube.com/watch?v=ri4flu1Jn4Y pdf download, si on veut download la convocation au lieu de l'afficher !
