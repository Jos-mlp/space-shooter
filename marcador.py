import pygame.font

class Marcador():
    """Clase para reportar informacion sobre puntuacion"""

    def __init__(self, ai_settings, pantalla, estadisticas):
        """Inicializa los atributos de registro de puntajes"""

        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        self.ai_settings = ai_settings
        self.estadisticas = estadisticas

        #Ajustes de fuente para la informacion de puntuacion
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepara la imagen del puntaje inicial
        self.prep_puntaje()
        self.prep_alto_puntaje()


    def prep_alto_puntaje(self):
        """Convierte el marcador en una imagen renderizada"""
        #Le agrega formato al marcador
        puntaje_alto = int(round(self.estadisticas.alto_puntaje, -1))
        alto_puntaje_str = "{:,}".format(puntaje_alto)

        #Renderiza en una imagen el marcador
        self.alto_puntaje_imagen = self.font.render(alto_puntaje_str, True, 
                    self.text_color, self.ai_settings.bg_color)
        
        #Centra el puntaje mas alto en la parte superior de la pantalla
        self.alto_puntaje_rect = self.alto_puntaje_imagen.get_rect()
        self.alto_puntaje_rect.right = self.pantalla_rect.centerx
        self.alto_puntaje_rect.top = self.puntaje_rect.top

    def prep_puntaje(self):
        """Convierte el marcador en una imagen renderizada"""
        #Le agrega formato al marcador
        puntaje_redondeado = int(round(self.estadisticas.puntaje, -1))
        puntaje_str = "{:,}".format(puntaje_redondeado)

        #Renderiza en una imagen el marcador
        self.puntaje_imagen = self.font.render(puntaje_str, True, 
                    self.text_color, self.ai_settings.bg_color)
        
        #Muestra el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_imagen.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20
    
    def draw_puntaje(self):
        """Dibuja la puntuacion en la pantalla"""
        self.pantalla.blit(self.puntaje_imagen, self.puntaje_rect)
        self.pantalla.blit(self.alto_puntaje_imagen, self.alto_puntaje_rect)