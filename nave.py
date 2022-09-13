import pygame

class Nave():
    """Sirve para manejar el comportamiento de la nave"""
    def __init__(self,pantalla):
        """Inicializa la nave y establece la posicion de partida"""
        self.pantalla = pantalla

        #Carga la imagen de la nave y obtiene su rectangulo(rect)
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #Comienza cada nave en la parte inferior y central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom - 5

    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""
        self.pantalla.blit(self.imagen,self.rect)


