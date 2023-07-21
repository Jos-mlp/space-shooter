class Estadisticas():
    """Seguimiento de las estadisticas de Invasion Alienigena"""
    def __init__(self,ai_settings):
        """Inicializa las estadisticas"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Inicia invasion alienigena en un estado activo
        self.game_active = False
        
    def reset_stats(self):
        """Incializa estadistias que pueden cambiar durante el juego"""    
        self.naves_restantes = self.ai_settings.cantidad_naves
        self.puntaje = 0