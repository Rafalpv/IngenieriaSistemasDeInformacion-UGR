import folium

# Crear un objeto de mapa centrado en una ubicación específica
mapa = folium.Map(location=[40.7128, -74.0060], zoom_start=20)

# Coordenadas de los puntos A y B
punto_a = [40.7128, -74.0060]
punto_b = [41.8781, -87.6298]

# Agregar un marcador para el punto A
folium.Marker(location=punto_a, popup='Punto A').add_to(mapa)

# Agregar un marcador para el punto B
folium.Marker(location=punto_b, popup='Punto B').add_to(mapa)

# Crear una línea entre los dos puntos
linea = folium.PolyLine(locations=[punto_a, punto_b], color='blue')

# Agregar la línea al mapa
linea.add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save('mapa.html')
