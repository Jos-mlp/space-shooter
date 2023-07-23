import pygame
from pygame.sprite import Sprite
from time import sleep

class Nave(Sprite):
    """Sirve para manejar el comportamiento de la nave"""
    def __init__(self,ai_settings,pantalla):
        """Inicializa la nave y establece la posicion de partida"""
        super(Nave, self).__init__()
        self.pantalla = pantalla
        self.ai_settings = ai_settings

        #Carga la imagen de la nave y obtiene su rectangulo(rect)
        self.image = pygame.image.load("imagenes/nave.png")
        self.rect = self.image.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #Comienza cada nave en la parte inferior y central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom - 5

        #Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)

        #Banderas de movimiento
        self.moving_right = False
        self.moving_left = False

        #Carga imagenes para la explosion
        self.images_diccionario = {}
        #Ciclo para cargar las imagenes
        for i in range(1 , 13):
            imageStr = "imagenes/explosion/" + str(i) + ".png"
            imagen = pygame.image.load(imageStr)
            image_explosion = pygame.transform.scale(imagen, (self.image.get_height(), self.image.get_width()))
            self.images_diccionario[i] = image_explosion

        #Carga sonido de la explosion


    def update(self):
        """Actualiza la posicion de la nave segun las banderas de movimiento"""
        if self.moving_right == True and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_settings.factor_velocidad_nave

        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.factor_velocidad_nave


        #Actualiza el objeto rect desde la variable self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""
        self.pantalla.blit(self.image,self.rect)
        

    def centrar_nave(self):
        """Centra la nave en la pantalla"""
        self.center = self.pantalla_rect.centerx
    
    def draw_explocion_nave(self, ai_settings):
        for clave, image in self.images_diccionario.items():
            self.pantalla.blit(image, self.rect)
            pygame.display.flip()  
            pygame.mixer.Sound.play(ai_settings.explosion)
            
            #Pausa
            sleep(0.1)
