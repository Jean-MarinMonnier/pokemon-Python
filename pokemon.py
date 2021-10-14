import random, os, time, msvcrt
from collections import Counter

# Déclarations 
randomCatchNumber = 0
randomNumber = 0
randomGetIndex = 0
listOfSpawnedPokemon = []
pokemonInventory = [
    {
        "name" : "Salamèche",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30,
        "attaque" : 7.5,
        "defense" : 7.5,
        "PV" : 7.5
    }
]
pokemonStorage = []
pokedollars = 10000
pokemon = [
    {
        "name" : "Pikachu",
        "percent" : 10,
        "counter" : 0,
        "resistance" : 25,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Aspiscot",
        "percent" : 60,
        "counter" : 0,
        "resistance" : 5,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Draco",
        "percent" : 2,
        "counter" : 0,
        "resistance" : 40,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Carapuce",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Salamèche",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Tortipous",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Ratata",
        "percent" : 80,
        "counter" : 0,
        "resistance" : 15,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Racaillou",
        "percent" : 30,
        "counter" : 0,
        "resistance" : 25,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Keunotor",
        "percent" : 25,
        "counter" : 0,
        "resistance" : 35,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Chenipan",
        "percent" : 75,
        "counter" : 0,
        "resistance" : 20,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
    {
        "name" : "Tortank",
        "percent" : 0.5,
        "counter" : 0,
        "resistance" : 50,
        "attaque" : 0,
        "defense" : 0,
        "PV" : 0
    },
]
ball = [
    {
        "name" : "PokeBall",
        "catchRate" : 30,
        "nbInInventory" : 10
    },
    {
        "name" : "SuperBall",
        "catchRate" : 50,
        "nbInInventory" : 0
    },
    {
        "name" : "HyperBall",
        "catchRate" : 70,
        "nbInInventory" : 0
    },
    {
        "name" : "MasterBall",
        "catchRate" : 100,
        "nbInInventory" : 5
    }
]

# Menu principal
def mainMenu():
    global pokedollars
    os.system('cls')
    action = int(input("Sélectionner l'action souhaitée : 1- Allez au Shop  2-Afficher l'inventaire  3- Allez chasser du Pokémon  4-Quitter "))
    if action == 1:
        os.system('cls')
        shop(ball)
    elif action == 2 :
        os.system('cls')
        showInventory()
    elif action == 3 :
        os.system('cls')
        goFindAPokemon()
    elif action == 4 :
        os.system('cls')
        exit()


#Fonctions Shop

# Séléction de la pokeball à acheter
def shop(pokeball):
    global pokedollars
    print("Votre solde :", pokedollars)
    chosenPokeball = int(input("Séléctionner une PokeBall à acheter : 1-Pokeball 200$  2-Superball 600$  3-Hyperball 1200$  4-Materball 50000$ "))
    if chosenPokeball == 1 :
        addBallToInventory(200, pokeball[chosenPokeball-1])
    elif chosenPokeball == 2 :
        addBallToInventory(600, pokeball[chosenPokeball-1])
    elif chosenPokeball == 3 :
        addBallToInventory(1200, pokeball[chosenPokeball-1])
    elif chosenPokeball == 4 :
        addBallToInventory (50000, pokeball[chosenPokeball-1])
    else :
        print("Touche Incorrecte")

# Ajout des pokeballs acheter, mise à jour du pokedollars, vérification si solde suffisant
def addBallToInventory(price, pokeball) :
    global pokedollars
    quantity = int(input("Choisir une quantité "))
    if quantity*price > pokedollars:
        print("Vous n'avez pas assez d'argent")
        time.sleep(2)
        os.system('cls')
        return shop(ball)
    else :
        pokeball["nbInInventory"] += quantity
        print("Merci de votre achat de",quantity, pokeball["name"])
        pokedollars -= quantity*price
        print("Nouveau solde : ", pokedollars,"$")
        time.sleep(4)
        mainMenu()



# Fonctions génération, capture, combat pokemon

# On fais spawn un pokemon et on affiche le menu d'action
def goFindAPokemon() :
    randomGetIndex = random.randint(0, len(pokemon)-1)
    spawnedPokemon = spawn(pokemon[randomGetIndex])
    menuChoice = int(input("Appuyer au choix sur : 1-Combattre   2-Capturer   3-Fuir "))
    if menuChoice == 1 :
        fight(pokemonInventory, spawnedPokemon)
        print("")
    elif menuChoice == 2 :
        catchPokemon(spawnedPokemon, ball)
    elif menuChoice == 3 : 
        print("Vous avez fuit \n")
    else :
        print("Touche incorrecte \n")
    mainMenu()

#  Prend un pokemon dans le liste, test si il apparait ou non, le retourne si oui
def spawn(pokemonToSpawn):
    randomNumber = random.randint(0, 100)
    if randomNumber <= pokemonToSpawn["percent"] :
        pokemonToSpawn = generatePokemonStats(pokemonToSpawn)
        print("Un ", pokemonToSpawn["name"], "SAUVAGE est appraru")
        # listOfSpawnedPokemon.append(pokemonToSpawn["name"])
        return pokemonToSpawn
    else :
        randomGetIndex = random.randint(0, len(pokemon)-1)
        return spawn(pokemon[randomGetIndex])

# Genère les stastisitiques d'attaque, de défense et PV du pokemon qui a spawn
def generatePokemonStats(pokethon):
    pokethon["attaque"] = random.randint(0, 15)
    pokethon["defense"] = random.randint(0, 15)
    pokethon["PV"] = random.randint(0, 15)
    return pokethon

# Gestion du combat entre 1 pokemon de l'inventaire et 1 qui a spawn
def fight(pokemonInventory, pokemonToAttack) :
    pokemonToSelect = ""
    global pokedollars
    j = 0
    for element in pokemonInventory:
        pokemonToSelect += str(j) +"-" + element["name"] + "  "
        j += 1
    print(pokemonToSelect)
    pokemonSelected = int(input("Sélectionnez un pokémon dans la liste "))
    ratio1 = int(pokemonInventory[pokemonSelected]["attaque"]/pokemonToAttack["defense"]*100)
    ratio2 = int(pokemonToAttack["attaque"]/pokemonInventory[pokemonSelected]["defense"]*100)
    maxNumber = ratio1 + ratio2
    winner = random.randint(0, maxNumber)
    if ratio1 > winner :
        print("Vous avez gagné !")
        pokedollars += random.randint(1, 2000)
        print("Nouveau solde : ", pokedollars, "$")
        time.sleep(3)
    elif ratio1 < winner : 
        print("Vous avez perdu")
        time.sleep(3)
    else :
        print("Égalité")
        time.sleep(3)

# Gestion de la capture du pokemon qui a spawn
def catchPokemon(pokemon, ball):
    randomCatchNumber = random.randint(0, 100)
    pokeBallType = int(input("Choisir le type de PokeBall :  1-PokeBall   2-SuperBall   3-HyperBall   4-MasterBall "))
    if ball[pokeBallType-1]["nbInInventory"] > 0 :
        tryCatch = ball[pokeBallType-1]["catchRate"]/(1 +(pokemon["resistance"]/100))
        ball[pokeBallType-1]["nbInInventory"] -= 1
        pokemonToAddToInventory = {
            "name" : pokemon["name"],
            "percent" : pokemon["percent"],
            "counter" : pokemon["counter"],
            "resistance" : pokemon["resistance"],
            "attaque" : pokemon["attaque"],
            "defense" : pokemon["defense"],
            "PV" : pokemon["PV"]
        }
        if ball[pokeBallType-1]["name"] == "MasterBall" :
            if len(pokemonInventory) < 6 :
                pokemonInventory.append(pokemonToAddToInventory)  
            else :
                pokemonStorage.append(pokemonToAddToInventory)  
            return print(pokemon["name"], "capturé avec succès"), time.sleep(5)
        elif randomCatchNumber <= tryCatch :
            pokemonInventory.append(pokemon)
            return print(pokemon["name"], "capturé avec succès"), time.sleep(5)
        else :
            return print("Le pokémon s'est échappé"), time.sleep(3)
    else :
        print("Vous n'avez pas de", ball[pokeBallType-1]["name"]), time.sleep(2)
        catchPokemon(pokemon, ball)



# Fonction inventaire

# Affichage des éléments de l'inventaire
def showInventory() :
    pokeBallInfosToShow = ""
    pokemonInventoryInfosToshow = ""
    pokemonStorageInfosToshow = ""
    stayInInventory = True
    for element in ball:
        pokeBallInfosToShow += element["name"] + " : " + str(element["nbInInventory"]) + "   "
    for element in pokemonInventory :
        pokemonInventoryInfosToshow += "  " + element["name"] +":  Attaque : "+ str(element["attaque"]) +"   Défense : "+ str(element["defense"]) +"   PV : "+ str(element["PV"]) + "\n"
    for element in pokemonStorage :
        pokemonStorageInfosToshow += "  " + element["name"] +":  Attaque : "+ str(element["attaque"]) +"   Défense : "+ str(element["defense"]) +"   PV : "+ str(element["PV"]) + "\n"
    print("PokeDollars : ", pokedollars)
    print(pokeBallInfosToShow)
    print("Pokémon dans l'inventaire : \n", pokemonInventoryInfosToshow)
    print("Pokémon dans le stockage : \n", pokemonStorageInfosToshow)
    print("\n \n Appuyez sur 'Échap' pour retourner au menu")
    while stayInInventory == True:
        if msvcrt.kbhit() and msvcrt.getch()[0] == 27 :
            stayInInventory = False
            mainMenu()
    


# Execute
mainMenu()









#Update des % de spawn dans le counter
# index = 0
# countNbOfPokemons = Counter(listOfSpawnedPokemon)
# for element in countNbOfPokemons:
#     pokemon[index]['counter'] = (countNbOfPokemons[pokemon[index]['name']]/10000)*100
#     index += 1



