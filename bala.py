from typing import Any
import pygame 
from pygame.sprite import Sprite

class Bala(Sprite):
    """Sirve para manejar las balas que dispara la nave"""
    def __init__(self, ai_settings,pantalla,nave):
        super (Bala,self).__init__()
        self.pantalla = pantalla

        #Crea una bala rectangular en (0,0) y luego establece 
        # la posicion correcta
        self.imagen = pygame.image.load("imagenes/B1.png")
        self.rect = self.imagen.get_rect()
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        #Almacena la posicion de la bala como un valor decimal 
        self.y = float(self.rect.y)
        self.factor_velocidad = ai_settings.bala_factor_velocidad

    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""
        # Actualiza la posicion decimal de la bala en y
        self.y -= self.factor_velocidad
        #Actualiza la posicion del rect
        self.rect.y = self.y
    
    def draw_bala(self):
        """Dibuja la bala en la pantalla"""
        self.pantalla.blit(self.imagen,self.rect)
        
