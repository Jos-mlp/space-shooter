import pygame
from pygame.sprite import Group
from settings import Settings
from estadisticas import Estadisticas
from nave import Nave
import funciones_juego as fj

def run_game():
    #Inicializamos el juego y creamos un objeto pantalla
    pygame.init()
    ai_settings = Settings() #Inicializamos las configuraciones y las guardamos en ai_settings
    pantalla = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Invasion alienigena")   

    #Crea una instancia para almacenar estadisticas del juego
    estadisticas = Estadisticas(ai_settings) 

    #Crea una nave, un grupo de aliens y un grupo de balas
    nave = Nave(ai_settings,pantalla)
    aliens = Group()
    balas = Group()
    
    #Crea la flota de aliens
    fj.crear_flota(ai_settings,nave, pantalla, aliens)

    #Inicializa el bucle principal del juego
    while True:
        #Escuchar eventos de teclado o raton
        fj.vericar_eventos(ai_settings,pantalla,nave, balas) 
        #Actualiza la posicion de la nave en respuesta a los eventos(segun las teclas que presione el jugador)
        nave.update()
        #Actualiza pocision bala y elimina balas
        fj.update_balas(ai_settings,nave, pantalla, aliens, balas)
        #Actualiza posicion aliens
        fj.update_aliens(ai_settings,estadisticas,pantalla,nave,aliens,balas)
        #Esto actualiza la pantalla en la funcion actualizar
        fj.actualizar_pantalla(ai_settings,pantalla,nave,aliens,balas)

if __name__ == "__main__":
    run_game()