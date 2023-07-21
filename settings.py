class Settings():
    """Sirve para almacenar todas las configuraciones"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (230,230,230)
        
        #Configuracion de la nave
        self.cantidad_naves = 3
        
        #Configuraciones de las balas
        self.balas_allowed = 3

        #Configuraciones de Alien
        self.fleet_drop_speed = 10

        #Que tan rapido se acelera el jurgo
        self.escala_aceleracion = 1.1

        self.inicializa_configuraciones_dinamicas()

    def inicializa_configuraciones_dinamicas(self):
        """Inicializa la configuracion que cambia en ejecucion"""
        #Configuracion de la nave
        self.factor_velocidad_nave = 1.5
        
        #Configuraciones de las balas
        self.bala_factor_velocidad = 1

        #Configuraciones de Alien
        self.alien_speed_factor = 1

        #fleet_direction,(si es 1 representa derecha), (si es -1 representa izquierda)
        self.fleet_direction= 1

        #Puntuacion
        self.puntos_alien = 50

    def aumentar_velocidad(self):
        """Aumenta la configuracion de velocidad"""
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.alien_speed_factor *= self.escala_aceleracion