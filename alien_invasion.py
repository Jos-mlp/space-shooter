import sys
import pygame

def run_game():
    pygame.init()
    #Creamos y cambiamos el nombre de la pantalla de nuestro juego
    pantalla = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Invasion alienigena") 

    while True:
        #Con el ciclo for detectamos todos los eventos que suceden dentro de pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Actualiza a la pantalla mas reciente
        pygame.display.flip()

if __name__ == "__main__":
    run_game()