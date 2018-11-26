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

world_gen_matrix = [
    [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
    [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
    [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
]

world_matrix = worldLocations.generate_world(world_gen_matrix)
print(world_matrix[1][1].name)

myPosition = world_matrix[1][1]
player_state = testParser.PlayerState(myPosition)

textinput = textInput.TextInput("", "pixelFont.ttf", 35, True, (255, 255, 255), 10, 10)

pygame.font.init()
labelFont = pygame.font.Font("pixelFont.ttf", 35)
promptLabel = labelFont.render('Enter a command: ', False, (255, 255, 255))
commandLabel = labelFont.render('', False, (255, 255, 255))

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
    
    gameDisplay.blit(promptLabel, (0, 650))
    gameDisplay.blit(commandLabel, (0, 750))

    events = pygame.event.get()
    for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False   

    input_text = ""
    output_text = ""
    if textinput.update(events):
        input_text = textinput.get_text()
        textinput.clear_text()
        output_text = testParser.text_parser(input_text, player_state)
        print("output text: " + output_text)

        commandLabel = labelFont.render(output_text, False, (255, 255, 255))

    gameDisplay.blit(textinput.get_surface(), (0, 695))
            
    pygame.display.update()
    # if player_state.room.get_text() != "":
    # print(player_state.room.get_text())
    gameDisplay.blit(commandLabel, (0, 750))

