import pygame
from settings import Settings
from nave import Nave
import funciones_juego as fj

def run_game():
    #Inicializamos el juego y creamos un objeto pantalla
    pygame.init()
    ai_settings = Settings() #Inicializamos las configuraciones y las guardamos en ai_settings
    pantalla = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Invasion alienigena")   

    #Crea una nave
    nave = Nave(ai_settings,pantalla)

    while True:
        #Escuchar eventos de teclado o raton
        fj.vericar_eventos(nave) 
        #Actualiza la posicion de la nave en respuesta a los eventos(segun las teclas que presione el jugador)
        nave.update()       
        #Esto actualiza la pantalla en la funcion actualizar
        fj.actualizar_pantalla(ai_settings,pantalla,nave)

if __name__ == "__main__":
    run_game()