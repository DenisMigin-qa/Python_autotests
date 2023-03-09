import requests
import pytest

token = '70dc49c8a90c7dcdecc1a0903c6b8b45'
response_reg_trainer = requests.post('https://pokemonbattle.me:9104//trainers/reg', 
            headers = {'Content-Type' : 'application/json'}, 
            json = {"trainer_token": token, "email": "mda2704@yandex.ru", "password": "Iloveqa1"})
print(response_reg_trainer.text)


response_confirm_email = requests.post('https://pokemonbattle.me:9104//trainers/confirm_email', 
            headers = {'Content-Type' : 'application/json'}, 
            json = {"trainer_token": token})
print(response_confirm_email.text)


response_create_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', 
            headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
            json = {"name": "Бульба", "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(response_create_pokemon.text)


response_change_name = requests.put('https://pokemonbattle.me:9104/pokemons', 
            headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
            json = {"pokemon_id": 6041, "name": "Lopux", "photo": ""})
print(response_change_name.text)

response_catch = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
            headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, 
            json = {"pokemon_id": 6041})
print(response_catch.text)