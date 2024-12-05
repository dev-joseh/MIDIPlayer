# import pygame
# import pygame.mixer
# import pygame.time
# import random
# from settings import WIDTH,HEIGHT,BACKGROUND_COLOR,MAX_FRAMERATE


# # Inicialize o pygame
# pygame.init()
# pygame.mixer.init()
# clock = pygame.time.Clock()

# # Configurações da tela
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# screen.fill(BACKGROUND_COLOR)

# def airbrush():
#     airbrush = True
#     cur = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     if click[0] == True: # evaluate left button
#         pygame.draw.circle(screen, (random.randrange(255),random.randrange(255),random.randrange(255),70), (cur[0] + random.randrange(-60,60), cur[1] + random.randrange(-60,60)), random.randrange(0, 5))

# # Loop principal do programa
# running = True
# while running:
#     clock.tick(MAX_FRAMERATE)
#     for event in pygame.event.get():
        
#         if event.type == pygame.QUIT:
#             running = False
        
#         #elif event.type == pygame.MOUSEBUTTONDOWN:
        
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 print('enter_pressed')
#             elif event.key == pygame.K_BACKSPACE:
#                 print('backspace_pressed')
#             else:
#                 print(f'{event.unicode} pressed')

#     airbrush()
#     pygame.display.flip()

# pygame.quit()

from ui.Interface import Interface

if __name__ == '__main__':
    interface = Interface()
    interface.run()