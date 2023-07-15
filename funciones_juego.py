import sys
import pygame
from bala import Bala
from alien import Alien

def verificar_eventos_keydown(event, ai_settings,pantalla,nave,balas):
    """Responde a las pulsaciones de las teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_settings,pantalla,nave,balas)
    elif event.key == pygame.K_q:
        sys.exit()

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

    

def actualizar_pantalla(ai_settings,pantalla,nave,aliens,balas):
    """Actualiza las imagenes en la pantalla y pasa a la nueva pantalla"""
    #Cambia color de fondo 
    pantalla.fill(ai_settings.bg_color)

    #vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    #Dibuja la nave sobre la pantalla
    nave.blitme()
    #Dibuja en la pantalla cada alien en el grupo dependiendo el rect
    aliens.draw(pantalla)

    #Actualiza a la pantalla mas reciente
    pygame.display.flip()

def update_balas(aliens, balas):
    """Actualiza la posicion de las balas y elimina las antiguas"""
    #Actualiza las posiciones de las balas
    balas.update()  

    #Elimina las balas antiguas
    for bala in balas.copy():
        if bala.rect.bottom <= 0 :
            balas.remove(bala) 
    
    #Comprueba si hay balas que hayan alcanzado a los aliens
    #Si es asi, se desaparece a la bala y al alien
    colisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    #True desaparece al objeto, false no desaparece al objeto del grupo


def fuego_bala(ai_settings,pantalla,nave,balas):
    """Dispara una bala si aun no ah alcanzado el limite"""
    #Crea una nueva bala y la agrega al grupo de balas
    if len(balas) < ai_settings.balas_allowed:
        nueva_bala = Bala(ai_settings, pantalla, nave)
        balas.add(nueva_bala)

def get_number_aliens_x(ai_settings,alien_width):
    """Determina el numero de alienigenas que caben en una fila"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 

def get_number_rows(ai_settings, nave_height, alien_height):
    """Determina el numero de filas de aliens que caben en la pantalal"""
    avalaible_space_y = (ai_settings.screen_height - (3 * alien_height)
                         - nave_height)
    number_rows = int(avalaible_space_y / (2 * alien_height))
    return number_rows

def crear_alien(ai_settings, pantalla, aliens,alien_number, row_number):
    """Crea un alien y lo coloca en la fila"""
    alien = Alien(ai_settings, pantalla)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    
    alien.rect.y = alien_height + (2 * alien_height * row_number)

    aliens.add(alien)

def crear_flota(ai_settings,nave, pantalla, aliens):
    """Crea una flota completa de alienigenas"""
    #Crea un alien y encuentra el numero de aliens seguidos
    #El espacio entre cada alien es igual al ancho de un alien
    alien = Alien(ai_settings,pantalla)
    number_aliens_x= get_number_aliens_x(ai_settings,alien.rect.width)

    number_rows = get_number_rows(ai_settings, nave.rect.height,alien.rect.height)
    
    #Crea la flota de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_settings, pantalla, aliens,alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
    """Responde de forma apropiada si algun alien llega a un borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
    

def change_fleet_direction(ai_settings,aliens):
    """Desciende toda la flota y cambia la direccion de la misma"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    


def update_aliens(ai_settings,aliens):
    """Comprueba si la flota esta al borde
    y actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()