import random
from collections import Counter

def spawn(pokemonToSpawn):
    randomNumber = random.randint(0, 100)
    if randomNumber <= pokemonToSpawn["percent"]:
        generatePokemonStats(pokemonToSpawn)
        return listeOfSpawnedPokemon.append(pokemonToSpawn["name"]), pokemonToSpawn
    else :
        randomGetIndex = random.randint(0, len(pokemon)-1)
        spawn(pokemon[randomGetIndex])

def generatePokemonStats(pokemon):
    pokemon["attaque"] = random.randint(0, 15)
    pokemon["defense"] = random.randint(0, 15)
    pokemon["PV"] = random.randint(0, 15)
    return pokemon

def catchPokemon(pokemon, ball, showSpawnMessage = True):
    randomCatchNumber = random.randint(0, 100)
    if showSpawnMessage == True :
        print("Un ", pokemon["name"], "SAUVAGE est apprarue")
    pokeBallType = int(input("Choisir le type de PokeBall : "))
    if ball[pokeBallType]["nbInInventory"] > 0 :
        tryCatch = ball[pokeBallType]["catchRate"]/(1 +(pokemon["resistance"]/100))
        ball[pokeBallType]["nbInInventory"] -= 1
        if ball[pokeBallType]["name"] == "MasterBall" :
            pokemonInventory.append(pokemon)      
            return print(pokemon["name"], "capturé avec succès")
        elif randomCatchNumber <= tryCatch :
            pokemonInventory.append(pokemon)
            return print(pokemon["name"], "capturé avec succès")
        else :
            return print("Le pokémon s'est échappé")
    else :
        print("Vous n'avez pas de", ball[pokeBallType]["name"])
        catchPokemon(pokemon, ball, False)
    


randomCatchNumber = 0
randomNumber = 0
randomGetIndex = 0
listeOfSpawnedPokemon = []
pokemonInventory = []
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
        "nbInInventory" : 0
    }
]

for i in range (0, 1):
    randomGetIndex = random.randint(0, len(pokemon)-1)
    spawn(pokemon[randomGetIndex])
    menuChoice = int(input("Appuyer au choix sur : 1-Combattre   2-Capturer   3-Fuir "))
    if menuChoice == 2:
        catchPokemon(pokemon[randomGetIndex], ball)


#Update des % de spawn dans le counter
index = 0
countNbOfPokemons = Counter(listeOfSpawnedPokemon)
for element in countNbOfPokemons:
    pokemon[index]['counter'] = (countNbOfPokemons[pokemon[index]['name']]/10000)*100
    index += 1



