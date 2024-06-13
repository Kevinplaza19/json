import xml.etree.ElementTree as ET

# Crear la estructura del XML
coleccion = ET.Element('coleccion')

pelicula1 = ET.SubElement(coleccion, 'pelicula')
ET.SubElement(pelicula1, 'titulo').text = 'El Padrino'
ET.SubElement(pelicula1, 'director').text = 'Francis Ford Coppola'
ET.SubElement(pelicula1, 'año_estreno').text = '1972'

pelicula2 = ET.SubElement(coleccion, 'pelicula')
ET.SubElement(pelicula2, 'titulo').text = 'Forrest Gump'
ET.SubElement(pelicula2, 'director').text = 'Robert Zemeckis'
ET.SubElement(pelicula2, 'año_estreno').text = '1994'

pelicula3 = ET.SubElement(coleccion, 'pelicula')
ET.SubElement(pelicula3, 'titulo').text = 'El Caballero Oscuro'
ET.SubElement(pelicula3, 'director').text = 'Christopher Nolan'
ET.SubElement(pelicula3, 'año_estreno').text = '2008'

pelicula4 = ET.SubElement(coleccion, 'pelicula')
ET.SubElement(pelicula4, 'titulo').text = 'Rapidos y furioso 4'
ET.SubElement(pelicula4, 'director').text = 'Justin Lin'
ET.SubElement(pelicula4, 'año_estreno').text = '2009'

# Convertir la estructura a un árbol ElementTree y escribir a un archivo
arbol = ET.ElementTree(coleccion)
arbol.write('peliculas.xml', encoding='utf-8', xml_declaration=True)

print("Archivo XML de películas creado con éxito.")
