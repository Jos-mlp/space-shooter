import sys
import pygame
from bala import Bala

def verificar_eventos_keydown(event, ai_settings,pantalla,nave,balas):
    """Responde a las pulsaciones de las teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Crea una nueva bala y la agrega al grupo de balas
        nueva_bala = Bala(ai_settings, pantalla, nave)
        balas.add(nueva_bala)

def verificar_eventos_keyup(event,nave):
    """Responde a cuando se sueltan las teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def vericar_eventos(ai_settings,pantalla,nave,balas):
    """Responde a las pulsaciones de teclas y los eventos del raton"""
    #Con el ciclo for detectamos todos los eventos(teclado o raton) que suceden dentro de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Registrar cuando se presiona una tecla
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event,ai_settings,pantalla,nave,balas)

        #Registra cuando se deja de presionar una tecla
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event,nave)

    

def actualizar_pantalla(ai_settings,pantalla,nave,balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva pantalla"""
    #Cambia color de fondo 
    pantalla.fill(ai_settings.bg_color)

    #vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    #Dibuja la nave sobre la pantalla
    nave.blitme()
    
    #Actualiza a la pantalla mas reciente
    pygame.display.flip()