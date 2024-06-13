import json

# Leer el archivo JSON
with open('peliculas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Recorrer los elementos del JSON
for pelicula in data['peliculas']:
    titulo = pelicula['titulo']
    director = pelicula['director']
    año_estreno = pelicula['año_estreno']
    
    print(f'Título: {titulo}')
    print(f'Director: {director}')
    print(f'Año de Estreno: {año_estreno}')
    print('---')

