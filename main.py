import pygame
import worldLocations
import textParser
import textInput
import playerState
import gameUpdate
from sys import exit

"""
    Description: Main function that runs the game loop. Handles updating text
    labels and other visuals

    Arguments:
        None
        
    Returns:
        None
"""

def main():

    HEIGHT = 790
    IMG_SIZE = 1920
    WIDTH = 640

    # Initializes the game clock
    clock = pygame.time.Clock()
    
    # Sets the width, height, image and caption for the game window
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TextVenture')
    my_image = pygame.image.load("images/map.PNG")

    # Renders the main game surface
    surf = pygame.Surface([IMG_SIZE, IMG_SIZE])
    
    # Initializes textInput to handle input text
    text_input = textInput.TextInput("", "pixelFont.ttf", 35, True,
                                    (255, 255, 255), 1000, 1000)
    
    # Initializes the font for all labels and sets up the labels
    pygame.font.init()
    labelFont = pygame.font.Font("pixelFont.ttf", 35)
    output_label1 = labelFont.render('', False, (255, 255, 255))
    output_label2 = labelFont.render('', False, (255, 255, 255))
    
    # Generates the game world and adds all sprites
    player_state = worldLocations.generate_world()
    player_state.gameDisplay = gameDisplay

    running = True

    # Displays a mini tutorial before beginning the game
    output_label1, output_label2, promptLabel = print_text('(Press any key to scroll) Welcome to TextVenture! Collect all the items and fight the evil demon in the north to win! To begin you can type \'go east\'', text_input, player_state)
    gameUpdate.update_main_screen(player_state)

    # Game loop
    while running:
        # Updates the command prompt label
        promptLabel = labelFont.render(textParser.get_prompt_label(player_state), False, (255, 255, 255))
        
        # Updates the textbox labels
        pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
        gameDisplay.blit(promptLabel, (0, 650))
        gameDisplay.blit(output_label1, (0, 690))
        gameDisplay.blit(output_label2, (0, 730))
        # Updates the screen as the user types
        gameDisplay.blit(text_input.get_surface(), (len(textParser.get_prompt_label(player_state)) * 21, 650))

        # Closes the window if the user presses the exit button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        input_text = " "
        # output_text = " "
        
        # Handles text input after enter is pressed
        if text_input.update(events):
            # Retrieves the text entered
            input_text = text_input.get_text()
            if not input_text == "":
                # Clears input line after pressing enter
                text_input.clear_text()
                # Runs the input text through the text parser and retrieves the output text
                output_text = textParser.text_parser(input_text, player_state)
                # Updates the strings to be displayed in the text
                output_label1, output_label2, promptLabel = print_text(output_text, text_input, player_state)

        # Updates all of the sprites and visuals on screen
        sprites = player_state.room.get_sprites()
        sprites.update()
        sprites.draw(gameDisplay)
        pygame.display.update()

        # Exits the window if the player dies
        if player_state.gameOver:
            pygame.time.delay(1000)
            running = False
            
    # Quits pygame after program completion
    pygame.display.quit()
    pygame.quit()


"""
    Description: Prints text to the text box
    
    Arguments:
        output_text: The text to be outputted on the display lines
        text_input: The text that the user types
        player_state: The current state of the player
        
    Returns:
        output_label1: The first display label with the newly updated text
        output_label2: The second display label with newly update text
        promptLabel: The prompt text
"""
def print_text(output_text, text_input, player_state):
    labelFont = pygame.font.Font("pixelFont.ttf", 35)
    gameDisplay = player_state.gameDisplay

    # Converts the text to be output into lines of a maximum width
    output_lines = text_input.print_lines(output_text)
    
    # Retreives the text for the prompt label
    promptLabel = labelFont.render(textParser.get_prompt_label(player_state), False, (255, 255, 255))
    output_label1 = ''
    output_label2 = ''
    
    # Only updates the text if there is text to be updated
    if output_lines != None:
        i = 0
        # Updates the lines of text, two at a time and waits for the user to
        # press a key before displaying the next lines
        while i < len(output_lines) - 1:
            # Draws a rectangle over the display text
            pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
            # Updates and displays the two lines of display text
            output_label1 = labelFont.render(output_lines[i], False, (255, 255, 255))
            output_label2 = labelFont.render(output_lines[i + 1], False, (255, 255, 255))
            gameDisplay.blit(output_label1, (0, 690))
            gameDisplay.blit(output_label2, (0, 730))
            gameDisplay.blit(promptLabel, (0, 650))
            
            # Keeps the sprites visible while waiting for a key press
            sprites = player_state.room.get_sprites()
            sprites.update()
            sprites.draw(gameDisplay)

            i += 1
            # If there are more than two lines of display text, wait for the
            # user to press a key before displaying additional lines
            if i > 1:
                while True:
                    # Waits for the user to press a key
                    e = pygame.event.wait()
                    if e.type == pygame.KEYDOWN:
                        break
            # Updates the screen
            pygame.display.update()

        pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
        
        # Ensures that the text remains visible by continually displaying the
        # last two lines of text that showed on screen until there is a new
        # update
        if len(output_lines) > 2:
            output_label1 = labelFont.render(output_lines[-2], False, (255, 255, 255))
            output_label2 = labelFont.render(output_lines[-1], False, (255, 255, 255))

        else:
            output_label1 = labelFont.render(output_lines[0], False, (255, 255, 255))
            output_label2 = labelFont.render(output_lines[1], False, (255, 255, 255))

        gameDisplay.blit(output_label1, (0, 690))
        gameDisplay.blit(output_label2, (0, 730))
        gameDisplay.blit(promptLabel, (0, 650))

    gameUpdate.update_main_screen(player_state)
    # Returns the text being displayed
    return output_label1, output_label2, promptLabel


# Runs main
if __name__ == "__main__":
    main()

