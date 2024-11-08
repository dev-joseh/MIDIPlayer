import pygame.mixer

# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para definir o volume da música
def set_volume(volume_level):
    """
    Ajusta o volume da música em reprodução.
    volume_level: float, valor entre 0.0 (mudo) e 1.0 (volume máximo)
    """
    if 0.0 <= volume_level <= 1.0:
        pygame.mixer.music.set_volume(volume_level)
        print(f"Volume ajustado para: {volume_level * 100}%")
    else:
        print("Erro: O valor do volume deve estar entre 0.0 e 1.0.")
    
# Função para obter o volume atual
def get_current_volume():
    """
    Retorna o volume atual da música.
    """
    return pygame.mixer.music.get_volume()
