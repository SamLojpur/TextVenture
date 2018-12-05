import pygame

"""
    Description: Updates the background image for the main screen based on the
    location of the player

    Arguments:
        player_state: The state of the player

    Returns:
        None
"""
def update_main_screen(player_state):
    my_image = pygame.image.load("images/map.PNG")
    # Retrieves the location of the player
    x = player_state.room.x
    y = player_state.room.y
    # Fills the background with a default colour, black
    player_state.gameDisplay.fill((0, 0, 0))
    # Displays the section of the map based on the (x,y) coordinates of the player
    player_state.gameDisplay.blit(my_image, [0, 0], [640*x, 640*y, 640, 640])


"""
    Description: Updates the text that is displayed in the game window

    Arguments:
        player_state: The state of the player
        promptLabel: The text that prompts the user to enter a command
        output_label1: The text to be displayed on the first output line of the
        text box

    Returns:
        None
"""
def update_text_box(player_state, promptLabel, output_label1, output_label2):
    # Fills the text box with default colour, black
    player_state.gameDisplay.fill((0, 0, 0))
    # Displays all three labels with the given (x, y) coordinates
    player_state.blit(promptLabel, (0, 650))
    player_state.gameDisplay.blit(outputLabel1, (0, 695))
    player_state.gameDisplay.blit(outputLabel2, (0, 735))
