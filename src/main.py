import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    while True:
        pokemon_id = random.randint(1, 350)
        pokemon_schema = fetch_pokemon_data(pokemon_id)
        if pokemon_schema:
            print(f'Adicionado {pokemon_schema.name} ao banco de dados.')
            add_pokemon_to_db(pokemon_schema)
        else:
            print(f'Não foi possível obter dados para o Pokemón com ID {pokemon_id}')
        time.sleep(10)

if __name__ == '__main__':
    main()
