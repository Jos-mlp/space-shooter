class Settings():
    """Sirve para almacenar todas las configuraciones"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #Configuracion de la nave
        self.factor_velocidad_nave = 1.5
        self.cantidad_naves = 3
        
        #Configuraciones de las balas
        self.bala_factor_velocidad = 1
        self.balas_allowed = 3

        #Configuraciones de Alien
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 20
        #fleet_direction,(si es 1 representa derecha), (si es -1 representa izquierda)
        self.fleet_direction= 1
        