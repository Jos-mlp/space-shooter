import pygame
from pygame.sprite import AbstractGroup, Sprite

class Alien(Sprite):
    """Sirve para representar a un solo alienigena en la flota"""
    def __init__(self, ai_settings, pantalla):
        """Inicializa el alien y establece su posicion inicial"""
        super(Alien, self).__init__()

        self.pantalla = pantalla
        self.ai_settings = ai_settings

        #Carga la imagen del aline y establece su rect
        self.image = pygame.image.load("imagenes/E1.png")
        self.rect = self.image.get_rect()

        #Inicia cada nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Almacena la posicion exacta del alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja el alien en su ubicacion actual"""
        self.pantalla.blit(self.image, self.rect)

    def check_edges(self):
        """Devuelve true si el alien esta en el borde de la pantalla"""
        screen_rect = self.pantalla.get_rect()
        if (self.rect.right > screen_rect.right):
            return True
        elif (self.rect.left < 0) :
            return True

    def update(self):
        """Mueve el aline a la derecha"""
        self.x += (self.ai_settings.alien_speed_factor * 
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x