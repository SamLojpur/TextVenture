import pygame

def update_main_screen(player_state):
    my_image = pygame.image.load("images/map.PNG")

    x = player_state.room.x
    y = player_state.room.y
    player_state.gameDisplay.fill((0, 0, 0))
    player_state.gameDisplay.blit(my_image, [0, 0], [640*x, 640*y, 640, 640])


def update_text_box(player_state, promptLabel, outputLabel1, outputLabel2):

    player_state.gameDisplay.fill((0, 0, 0))
    player_state.blit(promptLabel, (0, 650))
    player_state.gameDisplay.blit(outputLabel1, (0, 690))
    player_state.gameDisplay.blit(outputLabel2, (0, 730))