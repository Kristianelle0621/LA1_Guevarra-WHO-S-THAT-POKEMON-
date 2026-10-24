import random
import requests

url = 'https://pokeapi.co/api/v2/pokemon/ditto', 'https://pokeapi.co/api/v2/pokemon/pikachu',  'https://pokeapi.co/api/v2/pokemon/21'

x = requests.get(url)

print(x)