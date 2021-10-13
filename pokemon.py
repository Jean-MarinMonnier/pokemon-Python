import random
from collections import Counter

def spawn(pokemonToSpawn):
    randomNumber = random.randint(0, 100)
    if randomNumber <= pokemonToSpawn["percent"]:
        generatePokemonStats(pokemonToSpawn)
        print("Un ", pokemonToSpawn["name"], "SAUVAGE est apprarue")
        listeOfSpawnedPokemon.append(pokemonToSpawn["name"])
        print("pts", pokemonToSpawn)
        return pokemonToSpawn
    else :
        randomGetIndex = random.randint(0, len(pokemon)-1)
        return spawn(pokemon[randomGetIndex])

def generatePokemonStats(pokemon):
    pokemon["attaque"] = random.randint(0, 15)
    pokemon["defense"] = random.randint(0, 15)
    pokemon["PV"] = random.randint(0, 15)
    return pokemon

def catchPokemon(pokemon, ball):
    randomCatchNumber = random.randint(0, 100)
    pokeBallType = int(input("Choisir le type de PokeBall : "))
    if ball[pokeBallType]["nbInInventory"] > 0 :
        tryCatch = ball[pokeBallType]["catchRate"]/(1 +(pokemon["resistance"]/100))
        ball[pokeBallType]["nbInInventory"] -= 1
        if ball[pokeBallType]["name"] == "MasterBall" :
            print(len(pokemonInventory))
            if len(pokemonInventory) < 6 :
                pokemonInventory.append(pokemon)  
            else :
                pokemonStorage.append(pokemon)  
            return print(pokemon["name"], "capturé avec succès")
        elif randomCatchNumber <= tryCatch :
            pokemonInventory.append(pokemon)
            return print(pokemon["name"], "capturé avec succès")
        else :
            return print("Le pokémon s'est échappé")
    else :
        print("Vous n'avez pas de", ball[pokeBallType]["name"])
        catchPokemon(pokemon, ball)
    
def fight(pokemonInventory, pokemonToAttack, pokedollars) :
    pokemonToSelect = ""
    j = 0
    for element in pokemonInventory:
        pokemonToSelect += str(j) +" - " + element["name"]
        j += 1
    print(pokemonToSelect)
    pokemonSelected = int(input("Sélectionnez un pokémon dans la liste "))
    ratio1 = pokemonInventory[pokemonSelected]["attaque"]/pokemonToAttack["defense"]
    ratio2 = pokemonToAttack["attaque"]/pokemonInventory[pokemonSelected]["defense"]
    if ratio1 > ratio2 :
        print("Vous avez gagné !")
        pokedollars += random.randint(1, 2000)
    elif ratio2 > ratio1 : 
        print("Vous avez perdu")
    else :
        print("Égalité")
    print(pokedollars)


def addBallToInventory(price, pokeball) :
    quantity = int(input("Choisir une quantitée"))
    if quantity*price > pokedollars:
        print("Vous n'avez pas assez d'argent")
    else :
        pokeball["nbInInventory"] += quantity

def shop(pokeball):
    chosenPokeball = int(input("Séléctionner une Ball à acheter : 1-Pokeball 200$  2-Superball 600$  3-Hyperball 1200$  4-Materball 50000$"))
    if chosenPokeball == 1 :
        addBallToInventory(200, pokeball)
    elif chosenPokeball == 2 :
        addBallToInventory(600, pokeball)
    elif chosenPokeball == 3 :
        addBallToInventory(1200, pokeball)
    elif chosenPokeball == 4 :
        addBallToInventory (50000, pokeball)
    print(pokeball)


randomCatchNumber = 0
randomNumber = 0
randomGetIndex = 0
listeOfSpawnedPokemon = []
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
        "name" : "ratata",
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
        "nbInInventory" : 7
    }
]

def mainMenu():
    action = int(input("Sélectionner l'acion souhaitée : 1- Allez au Shop  2-Afficher l'inventaire  3- Allez chasser du Pokémon"))
    if action == 1:
        shop()

def goFindAPokemon() :
    randomGetIndex = random.randint(0, len(pokemon)-1)
    print("rgi", randomGetIndex)
    spawnedPokemon = spawn(pokemon[randomGetIndex])
    print("sp", spawnedPokemon)
    menuChoice = int(input("Appuyer au choix sur : 1-Combattre   2-Capturer   3-Fuir "))
    if menuChoice == 1 :
        fight(pokemonInventory, spawnedPokemon, pokedollars)
        print("")
    elif menuChoice == 2 :
        catchPokemon(spawnedPokemon, ball)
    elif menuChoice == 3 : 
        print("Vous avez fuit")
        print("")
        # continue
    else :
        print("Touche incorrecte")
    print("")

#Update des % de spawn dans le counter
index = 0
countNbOfPokemons = Counter(listeOfSpawnedPokemon)
for element in countNbOfPokemons:
    pokemon[index]['counter'] = (countNbOfPokemons[pokemon[index]['name']]/10000)*100
    index += 1



