import json

# Datos de las películas
peliculas = {
    "peliculas": [
        {
            "titulo": "El Padrino",
            "director": "Francis Ford Coppola",
            "año_estreno": 1972
        },
        {
            "titulo": "Forrest Gump",
            "director": "Robert Zemeckis",
            "año_estreno": 1994
        },
        {
            "titulo": "El Caballero Oscuro",
            "director": "Christopher Nolan",
            "año_estreno": 2008
        },
        {
            "titulo": "Rapidos y furioso 4",
            "director": "Justin Lin",
            "año_estreno": 2009
        }
    ]
}

# Escribir los datos en un archivo JSON
with open('peliculas.json', 'w', encoding='utf-8') as file:
    json.dump(peliculas, file, ensure_ascii=False, indent=4)

print("Archivo JSON de películas creado con éxito.")
