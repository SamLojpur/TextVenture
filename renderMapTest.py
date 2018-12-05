import pygame
import worldLocations
import testParser
import textInput
import playerState
import gameUpdate
from sys import exit

"""
    Description: Main function that runs the game loop
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
    textinput = textInput.TextInput("", "pixelFont.ttf", 35, True,
                                    (255, 255, 255), 1000, 1000)
    
    # Initializes the font for all labels and sets up the labels
    pygame.font.init()
    labelFont = pygame.font.Font("pixelFont.ttf", 35)
    outputLabel1 = labelFont.render('', False, (255, 255, 255))
    outputLabel2 = labelFont.render('', False, (255, 255, 255))
    
    # Generates the game world and adds all sprites
    player_state = worldLocations.generate_world()
    player_state.gameDisplay = gameDisplay

    running = True

    # Displays a mini tutorial before beginning the game
    outputLabel1, outputLabel2, promptLabel = print_text('(Press any key to scroll) Welcome to TextVenture! Collect all the items and fight the evil demon in the north to win! To begin you can type \'go east\'', textinput, player_state)
    gameUpdate.update_main_screen(player_state)

    # Game loop
    while running:
        # Updates the command prompt label
        promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))
        
        # Updates the textbox labels
        pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
        gameDisplay.blit(promptLabel, (0, 650))
        gameDisplay.blit(outputLabel1, (0, 690))
        gameDisplay.blit(outputLabel2, (0, 730))
        # Updates the screen as the user types
        gameDisplay.blit(textinput.get_surface(), (len(testParser.get_prompt_label(player_state)) * 21, 650))

        # Closes the window if the user presses the exit button
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        input_text = " "
        # output_text = " "
        
        # Handles text input after enter is pressed
        if textinput.update(events):
            # Retrieves the text entered
            input_text = textinput.get_text()
            # Clears input line after pressing enter
            textinput.clear_text()
            # Runs the input text through the text parser and retrieves the output text
            output_text = testParser.text_parser(input_text, player_state)
            # Updates the strings to be displayed in the text
            outputLabel1, outputLabel2, promptLabel = print_text(output_text, textinput, player_state)

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


def print_text(output_text, textinput, player_state):
    labelFont = pygame.font.Font("pixelFont.ttf", 35)
    gameDisplay = player_state.gameDisplay

    output_lines = textinput.print_lines(output_text)
    print("output text: " + output_text)

    promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))
    outputLabel1 = ''
    outputLabel2 = ''

    if output_lines != None:
        i = 0
        # f = True
        while i < len(output_lines) - 1:
            pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
            print("output text1: " + output_lines[i])
            outputLabel1 = labelFont.render(output_lines[i], False, (255, 255, 255))
            print("output text2: " + output_lines[i + 1])
            outputLabel2 = labelFont.render(output_lines[i + 1], False, (255, 255, 255))

            gameDisplay.blit(outputLabel1, (0, 690))
            gameDisplay.blit(outputLabel2, (0, 730))
            gameDisplay.blit(promptLabel, (0, 650))
            sprites = player_state.room.get_sprites()
            sprites.update()
            sprites.draw(gameDisplay)

            # pygame.display.update(outputLabel1)
            # pygame.time.delay(2000)

            i += 1
            if i > 1:
                while True:
                    e = pygame.event.wait()
                    if e.type == pygame.KEYDOWN:
                        break
            pygame.display.update()

        pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])
        if len(output_lines) > 2:
            print("output text1: " + output_lines[-2])
            outputLabel1 = labelFont.render(output_lines[-2], False, (255, 255, 255))
            print("output text2: " + output_lines[-1])
            outputLabel2 = labelFont.render(output_lines[-1], False, (255, 255, 255))

        else:
            print("output text1: " + output_lines[0])
            outputLabel1 = labelFont.render(output_lines[0], False, (255, 255, 255))
            print("output text2: " + output_lines[1])
            outputLabel2 = labelFont.render(output_lines[1], False, (255, 255, 255))

        gameDisplay.blit(outputLabel1, (0, 690))
        gameDisplay.blit(outputLabel2, (0, 730))
        gameDisplay.blit(promptLabel, (0, 650))

    gameUpdate.update_main_screen(player_state)
    return outputLabel1, outputLabel2, promptLabel



if __name__ == "__main__":
    main()

