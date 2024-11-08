import pygame
import pygame.mixer
from modules import volume_control  # Importa o módulo de controle de volume

# Inicialize o pygame
pygame.init()
pygame.mixer.init()

# Configurações da tela
width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Leitor de MIDI com Controle de Volume")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Caixa de texto para entrada do caminho do arquivo MIDI
input_box = pygame.Rect(50, 50, 500, 40)
color_inactive = GRAY
color_active = GREEN
color = color_inactive
active = False
text = ''

# Botão "Carregar"
button = pygame.Rect(250, 120, 100, 50)
button_text = font.render("Carregar", True, BLACK)

# Slider para controle de volume
slider_rect = pygame.Rect(50, 200, 500, 20)  # A barra do slider
slider_knob_rect = pygame.Rect(50, 190, 20, 40)  # O controle deslizante (knob)
volume_level = 0.5  # Volume inicial (50%)
volume_control.set_volume(volume_level)  # Ajusta o volume inicial

# Função para tocar o arquivo MIDI
def play_midi(file_path):
    try:
        pygame.mixer.music.load(f"playlist/{file_path}.mid")
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Erro ao carregar o arquivo MIDI: {e}")

# Função para atualizar o volume com base na posição do slider
def update_volume(mouse_x):
    global volume_level
    # Limitar a posição do slider para a barra
    if slider_rect.left <= mouse_x <= slider_rect.right:
        slider_knob_rect.centerx = mouse_x
        # Calculando o volume (0.0 a 1.0)
        volume_level = (mouse_x - slider_rect.left) / slider_rect.width
        volume_control.set_volume(volume_level)

# Loop principal do programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar se a caixa de entrada foi clicada
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            # Verificar se o botão "Carregar" foi clicado
            if button.collidepoint(event.pos):
                play_midi(text)
            # Verificar se o slider foi clicado
            if slider_rect.collidepoint(event.pos):
                update_volume(event.pos[0])
        elif event.type == pygame.MOUSEMOTION:
            # Se o mouse estiver pressionado, mover o knob do slider
            if event.buttons[0] == 1:  # Verifica se o botão esquerdo do mouse está pressionado
                if slider_rect.collidepoint(event.pos):
                    update_volume(event.pos[0])
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    play_midi(text)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Desenhar elementos da interface
    screen.fill(WHITE)

    # Atualizar a cor da caixa de entrada
    color = color_active if active else color_inactive

    # Caixa de entrada de texto
    pygame.draw.rect(screen, color, input_box, 2)
    txt_surface = font.render(text, True, BLACK)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    input_box.w = max(500, txt_surface.get_width() + 10)

    # Botão "Carregar"
    pygame.draw.rect(screen, GRAY, button)
    screen.blit(button_text, (button.x + 10, button.y + 10))

    # Desenhar o slider
    pygame.draw.rect(screen, BLACK, slider_rect)
    pygame.draw.rect(screen, GREEN, slider_knob_rect)  # O knob do slider

    # Atualizar o display
    pygame.display.flip()

pygame.quit()
