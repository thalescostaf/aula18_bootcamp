import requests

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/15')
data = response.json()
data_types = data['types']
type_list =[]
for type_info in data_types:
    type_list.append(type_info['type']['name'])
types = ', '.join(type_list)
print(data['name'],types)



