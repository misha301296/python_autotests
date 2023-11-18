import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
headers= {'Content-Type':'application/json', 'trainer_token': '4883e0d019e25f61ce116a5047d613c0'})
print(response.text)

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
json = {
"pokemon_id": "19788",
"name": "Kiryu",
"photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
headers= {'Content-Type':'application/json', 'trainer_token': '4883e0d019e25f61ce116a5047d613c0'})
print(response.text)

response = requests.post(url='https://api.pokemonbattle.me:9104//trainers/add_pokeball',
json = {
"pokemon_id": "19788",
},
headers= {'Content-Type':'application/json', 'trainer_token': '4883e0d019e25f61ce116a5047d613c0'})
print(response.text)