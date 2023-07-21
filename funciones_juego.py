import sys
from time import sleep
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

def vericar_eventos(ai_settings,pantalla,estadisticas,play_button,nave,aliens,balas):
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

        #Registra cuando se presiona el boton del mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,pantalla,estadisticas,play_button,nave,aliens,balas, mouse_x, mouse_y)

def check_play_button(ai_settings,pantalla,estadisticas,play_button,nave,aliens,balas, mouse_x, mouse_y):
    """Comienza un nuevo juego cuando el jugador da click en play"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not estadisticas.game_active:
        #Inicializa la configuracion del juego
        ai_settings.inicializa_configuraciones_dinamicas()
        
        #Ocultar el cursor del mouse
        pygame.mouse.set_visible(False)

        #Restablece las estadisticas del juego
        estadisticas.reset_stats()
        estadisticas.game_active = True

        #Vacia la lista de aliens y balas
        aliens.empty()
        balas.empty()

        #Crea una nueva flota y centra la nave
        crear_flota(ai_settings,nave, pantalla, aliens)
        nave.centrar_nave()

def actualizar_pantalla(ai_settings,pantalla,estadisticas
                    ,marcador,nave,aliens,balas,play_button):
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

    #Dibuja el boton de play si el juego esta inactivo
    if not estadisticas.game_active:
        play_button.draw_button()

    #Dibuja la informacion de la puntuacion
    marcador.draw_puntaje()
    
    #Actualiza a la pantalla mas reciente
    pygame.display.flip()

def update_balas(ai_settings,nave, pantalla
                    ,estadisticas,marcador, aliens, balas):
    """Actualiza la posicion de las balas y elimina las antiguas"""
    #Actualiza las posiciones de las balas
    balas.update()  

    #Elimina las balas antiguas
    for bala in balas.copy():
        if bala.rect.bottom <= 0 :
            balas.remove(bala) 
    
    check_bala_alien_collisions(ai_settings,nave, pantalla
                    ,estadisticas,marcador, aliens, balas)


def check_bala_alien_collisions(ai_settings,nave, pantalla
                    ,estadisticas,marcador, aliens, balas):
    """Responde a las colisiones entre balas y aliens"""
    #Elimina las balas y los aliens que colisionaron
    #True desaparece al objeto, false no desaparece al objeto del grupo
    colisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    
    if colisions:
        estadisticas.puntaje += ai_settings.puntos_alien
        marcador.prep_puntaje()
    
    if len(aliens)==0:
        #Destruye balas existentes y crea una nueva flota
        balas.empty()
        ai_settings.aumentar_velocidad()
        crear_flota(ai_settings,nave, pantalla, aliens)

def fuego_bala(ai_settings,pantalla,nave,balas):
    """Dispara una bala si aun no ah alcanzado el limite"""
    #Crea una nueva bala y la agrega al grupo de balas
    if len(balas) < ai_settings.balas_allowed:
        nueva_bala = Bala(ai_settings, pantalla, nave)
        balas.add(nueva_bala)
        #Reproduce el sonido del disparo de la nueva bala
        pygame.mixer.Sound.play(nueva_bala.disparo)

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

def nave_golpeada(ai_settings,estadisticas,pantalla,nave,aliens,balas):
    """Responde a una nave siendo golpeada por un alien"""
    if estadisticas.naves_restantes > 0:
        #Disminuye naves restantes
        estadisticas.naves_restantes -= 1

        #Vacia la lista de aliens y balas
        aliens.empty()
        balas.empty()

        #Crea una nueva flota y centra la nave
        crear_flota(ai_settings,nave, pantalla, aliens)
        nave.centrar_nave()

        #Pausa
        sleep(0.5)
    else:
        estadisticas.game_active = False

        #Muestra el cursor del mouse
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,estadisticas,pantalla,nave,aliens,balas):
    """Comprueba si algun alien ha llegado al final de la pantalla"""
    pantalla_rect = pantalla.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= pantalla_rect.bottom:
            #Trata esto de la misma forma que si la nave fuera golpeada
            nave_golpeada(ai_settings,estadisticas,pantalla,nave,aliens,balas)

def update_aliens(ai_settings,estadisticas,pantalla,nave,aliens,balas):
    """Comprueba si la flota esta al borde
    y actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #Busca colisiones de nave-alien
    if pygame.sprite.spritecollide(nave, aliens,False):
        nave_golpeada(ai_settings,estadisticas,pantalla,nave,aliens,balas)
    
    #Busca aliesn que golpean la parte inferior de la pantalla
    check_aliens_bottom(ai_settings,estadisticas,pantalla,nave,aliens,balas)