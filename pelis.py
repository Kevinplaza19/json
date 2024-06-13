import xml.etree.ElementTree as ET

# Leer el archivo XML
arbol = ET.parse('peliculas.xml')
raiz = arbol.getroot()

# Recorrer los elementos del XML
for pelicula in raiz.findall('pelicula'):
    titulo = pelicula.find('titulo').text
    director = pelicula.find('director').text
    año_estreno = pelicula.find('año_estreno').text
    
    print(f'Título: {titulo}')
    print(f'Director: {director}')
    print(f'Año de Estreno: {año_estreno}')
    print('---')
