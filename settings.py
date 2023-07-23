import pygame
class Settings():
    """Sirve para almacenar todas las configuraciones"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        #configuracionde la pantalla
        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (0,0,0)
        self.imagen_fondo = pygame.image.load("imagenes/fondo3.jpg")
        self.image = pygame.transform.scale(self.imagen_fondo, (self.screen_width, self.screen_height))
        self.image_pantalla_rect = self.image.get_rect() 
        self.title_window = "Invasion Alienigena"
        
        #Configuracion de la nave
        self.cantidad_naves = 3
        self.explosion = pygame.mixer.Sound("sound/explosion.wav")
        
        #Configuraciones de las balas
        self.balas_allowed = 3
        self.disparo = pygame.mixer.Sound("sound/laser.wav")

        #Configuraciones de Alien
        self.fleet_drop_speed = 15
        self.golpe = pygame.mixer.Sound("sound/golpe.wav")

        #Que tan rapido se acelera el juego
        self.escala_aceleracion = 1.1

        #Que tan rapido aumentan los valores de puntos por alien
        self.escala_puntaje = 1.5
        
        self.inicializa_configuraciones_dinamicas()

    def inicializa_configuraciones_dinamicas(self):
        """Inicializa la configuracion que cambia en ejecucion"""
        #Configuracion de la nave
        self.factor_velocidad_nave = 0.5
        
        #Configuraciones de las balas
        self.bala_factor_velocidad = 0.5

        #Configuraciones de Alien
        self.alien_speed_factor = 0.5

        #fleet_direction,(si es 1 representa derecha), (si es -1 representa izquierda)
        self.fleet_direction= 1

        #Puntuacion
        self.puntos_alien = 50

    def aumentar_velocidad(self):
        """Aumenta la configuracion de velocidad y los valores de puntos por alien"""
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.alien_speed_factor *= self.escala_aceleracion
        
        self.puntos_alien = int(self.puntos_alien * self.escala_puntaje)
        