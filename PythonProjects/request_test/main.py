import requests


website = "https://api.pokemonbattle.me:9104/trainers/reg"
response = requests.post(website, json={

    "trainer_token": "bf0beae92e7b2c6665b823c4d1971d81",
    "email": "adnz0@waterisgone.com",
    "password": "Antonstefankov1999",


}, headers={"Content-Type" : "application/json"})
print(response.text)


import requests


website = "https://api.pokemonbattle.me:9104/trainers/confirm_email"
response = requests.post(website, json={

    "trainer_token": "bf0beae92e7b2c6665b823c4d1971d81"


}, headers={"Content-Type" : "application/json"})
print(response.text)



import requests


website = "https://api.pokemonbattle.me:9104/pokemons"
response = requests.post(website, json={


    "name": "Кролик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"



}, headers={"Content-Type" : "application/json", "trainer_token": "bf0beae92e7b2c6665b823c4d1971d81"})
print(response.text)




import requests


website = "https://api.pokemonbattle.me:9104/pokemons"
response = requests.post(website, json={


    "pokemon_id": "12412",
    "name": "Antoshka",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"



}, headers={"Content-Type" : "application/json", "trainer_token": "bf0beae92e7b2c6665b823c4d1971d81"})
print(response.text)



import requests


website = "https://api.pokemonbattle.me:9104/trainers/add_pokeball"
response = requests.post(website, json={



    "pokemon_id": "12412"




}, headers={"Content-Type" : "application/json", "trainer_token": "bf0beae92e7b2c6665b823c4d1971d81"})
print(response.text)





