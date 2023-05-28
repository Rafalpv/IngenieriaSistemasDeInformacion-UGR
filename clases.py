class Combustible:
    def __init__(self, nombre, precio_litro_actual, precio_litro_pasado, precio_litro_maxHistorico):
        self.nombre = nombre
        self.precio_litro_actual = precio_litro_actual
        self.precio_litro_pasado = precio_litro_pasado
        self.precio_litro_maxHistorico = precio_litro_maxHistorico
        
class Entidad:
    def __init__(self, combustibles, imagen_link):
        self.combustibles = combustibles
        self.imagen_link = imagen_link
    
class Gasolinera:
    def __init__(self,nombre,municipio,cod_postal,ubicacion,combustibles):
        self.nombre = nombre
        self.municipio = municipio
        self.cod_postal = cod_postal
        self.ubicacion = ubicacion
        self.combustibles = combustibles
    
class Ruta:
    def __init__(self,ciudad_partida,ciudad_destino,gasolineras):
        self.ciudad_partida = ciudad_partida
        self.ciudad_destino = ciudad_destino
        self.gasolineras = gasolineras
        