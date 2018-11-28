import pygame
import worldLocations
import testParser
import textInput

# @todo add constants
# @todo get pycharm KATE

# pygame.init()
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((640, 790))
pygame.display.set_caption('World')

my_image = pygame.image.load("images/map.PNG")

surf = pygame.Surface([1920, 1920])

player_state = worldLocations.generate_world()

textinput = textInput.TextInput("", "pixelFont.ttf", 35, True, (255, 255, 255), 400, 400)

pygame.font.init()
labelFont = pygame.font.Font("pixelFont.ttf", 35)
# promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))
outputLabel1 = labelFont.render('', False, (255, 255, 255))
outputLabel2 = labelFont.render('', False, (255, 255, 255))

running = True
while running:
    # @todo move stuff to separate function for textbox
    # @todo make textbox multiline

    pygame.event.get()

    x = player_state.room.x
    y = player_state.room.y
    
    # print(x)
    # print(y)
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(my_image, [0, 0], [640*x, 640*y, 640, 640])
    
    promptLabel = labelFont.render(testParser.get_prompt_label(player_state), False, (255, 255, 255))
        
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


    input_text = ""
    output_text = " "
    if textinput.update(events):
        input_text = textinput.get_text()
        textinput.clear_text()
        output_text = testParser.text_parser(input_text, player_state)
        output_lines = textinput.print_lines(output_text)
        print("output text: " + output_text)
        if output_lines != None:
            outputLabel1 = labelFont.render(output_lines[0], False, (255, 255, 255))
            outputLabel2 = labelFont.render(output_lines[1], False, (255, 255, 255))
        
        
    sprites = player_state.room.render_room()
    sprites.update()
    sprites.draw(gameDisplay)        

    pygame.display.update()
    
    
    # if player_state.room.get_text() != "":
    # print(player_state.room.get_text())
    #gameDisplay.blit(commandLabel, (0, 750))

pygame.display.quit() 
pygame.quit()
