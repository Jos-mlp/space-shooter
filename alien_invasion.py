import sys
import pygame
from settings import Settings
from nave import Nave

def run_game():
    #Inicializamos el juego y creamos un objeto pantalla
    pygame.init()
    ai_settings = Settings() #Inicializamos las configuraciones y las guardamos en ai_settings
    pantalla = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Invasion alienigena")   

    #Crea una nave
    nave = Nave(pantalla)

    while True:
        #Con el ciclo for detectamos todos los eventos(teclado o raton) que suceden dentro de pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Cambia color de fondo 
        pantalla.fill(ai_settings.bg_color)
        #Dibuja la nave sobre la pantalla
        nave.blitme()
        
        #Actualiza a la pantalla mas reciente
        pygame.display.flip()

if __name__ == "__main__":
    run_game()