import pygame
import worldLocations
import testParser
import textInput
import playerState
import gameUpdate

def main():

    HEIGHT = 790
    IMG_SIZE = 1920
    WIDTH = 640

    # pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('World')

    my_image = pygame.image.load("images/map.PNG").convert()
    gameDisplay.set_alpha(255)


     #player_state = worldLocations.generate_world()
     #player_state.gameDisplay = gameDisplay

    surf = pygame.Surface([IMG_SIZE, IMG_SIZE])

    textinput = textInput.TextInput("", "pixelFont.ttf", 35, True, (255, 255, 255), 1000, 1000)

    pygame.font.init()
    labelFont = pygame.font.Font("pixelFont.ttf", 35)
    # promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))
    outputLabel1 = labelFont.render('', False, (255, 255, 255))
    outputLabel2 = labelFont.render('', False, (255, 255, 255))

    """
    x = textinput.print_lines("The bunny can't talk. It is very cute though. I need to fill another line")
    if x != None:
        for i in range(0, len(x)):
            print(x[i])
            """


    player_state = worldLocations.generate_world()
    player_state.gameDisplay = gameDisplay

    running = True


    outputLabel1, outputLabel2, promptLabel = print_text('(Press any key to scroll) Welcome to TextVenture! Collect all the items and fight the evil demon in the north to win! To begin you can type \'go east\'', textinput, player_state)
    gameUpdate.update_main_screen(player_state)

    while running:

        #update_screen(player_state)

        #x = player_state.room.x
        #y = player_state.room.y

        #gameDisplay.fill((0, 0, 0))
        #gameDisplay.blit(my_image, [0, 0], [640*x, 640*y, 640, 640])


        promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))

        pygame.draw.rect(gameDisplay, (0, 0, 0), [0, 640, 640, 790])

        gameDisplay.blit(promptLabel, (0, 650))
        gameDisplay.blit(outputLabel1, (0, 690))
        gameDisplay.blit(outputLabel2, (0, 730))

        # Small bug here, after entering first command, input flashes before disappearing
        gameDisplay.blit(textinput.get_surface(), (len(testParser.get_prompt_label(player_state)) * 21, 650))


        # Process exit event
        events = pygame.event.get()
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False




        input_text = " "
        # output_text = " "
        if textinput.update(events):
            input_text = textinput.get_text()
            textinput.clear_text()
            output_text = testParser.text_parser(input_text, player_state)

            outputLabel1, outputLabel2, promptLabel = print_text(output_text, textinput, player_state)

        sprites = player_state.room.get_sprites()
        sprites.update()
        sprites.draw(gameDisplay)
        pygame.display.update()

        if player_state.gameOver:
            main()

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

