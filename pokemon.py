import random
from collections import Counter

def spawn(name, percent,):
    randomNumber = random.randint(0, 100)
    if randomNumber <= percent:
        return listeOfSpawnedPokemon.append(name)
    else :
        # listeOfSpawnedPokemon.append(0)
        randomGetIndex = random.randint(0, len(pokemon)-1)
        spawn(pokemon[randomGetIndex].get('name'), pokemon[randomGetIndex].get('percent'))

def catchPokemon():
    

randomCatchNumber
randomNumber = 0
randomGetIndex = 0
listeOfSpawnedPokemon = []
pokemon = [
    {
        "name" : "Pikachu",
        "percent" : 10,
        "counter" : 0,
        "resistance" : 25
    },
    {
        "name" : "Aspiscot",
        "percent" : 60,
        "counter" : 0,
        "resistance" : 5
    },
    {
        "name" : "Draco",
        "percent" : 2,
        "counter" : 0,
        "resistance" : 40
    },
    {
        "name" : "Carapuce",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30
    },
    {
        "name" : "Salamèche",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30
    },
    {
        "name" : "Tortipous",
        "percent" : 5,
        "counter" : 0,
        "resistance" : 30
    },
    {
        "name" : "ratata",
        "percent" : 80,
        "counter" : 0,
        "resistance" : 15
    },
    {
        "name" : "Racaillou",
        "percent" : 30,
        "counter" : 0,
        "resistance" : 25
    },
    {
        "name" : "Keunotor",
        "percent" : 25,
        "counter" : 0,
        "resistance" : 35
    },
    {
        "name" : "Chenipan",
        "percent" : 75,
        "counter" : 0,
        "resistance" : 20
    },
    {
        "name" : "Tortank",
        "percent" : 0.5,
        "counter" : 0,
        "resistance" : 50
    },
]
ball = [
    {
        "name" : "PokeBall",
        "catchRate" : 30
    },
        {
        "name" : "SuperBall",
        "catchRate" : 50
    },
        {
        "name" : "HyperBall",
        "catchRate" : 70
    },
        {
        "name" : "MasterBall",
        "catchRate" : 100
    }
]

for i in range (0, 10000):
    randomGetIndex = random.randint(0, len(pokemon)-1)
    spawn(pokemon[randomGetIndex].get('name'), pokemon[randomGetIndex].get('percent'))

countNbOfPokemons = Counter(listeOfSpawnedPokemon)

index = 0
for element in countNbOfPokemons:
    pokemon[index]['counter'] = (countNbOfPokemons[pokemon[index]['name']]/10000)*100
    print(pokemon[index])
    index += 1


# print(listeOfSpawnedPokemon)
# print(pokemon[randomGetIndex].get('counter'))




