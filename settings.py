class Settings():
    """Sirve para almacenar todas las configuraciones"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #Configuracion de la nave
        self.factor_velocidad_nave = 1.5
        
        #Configuraciones de las balas
        self.bala_factor_velocidad = 1