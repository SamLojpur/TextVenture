import pygame
import worldLocations
import testParser

# pygame.init()
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((305, 305))
pygame.display.set_caption('World')

my_image = pygame.image.load("images/map.png")

surf = pygame.Surface([305, 305])

world_gen_matrix = [
    [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
    [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
    [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
]

world_matrix = worldLocations.generate_world(world_gen_matrix)
print(world_matrix[1][1].name)

myPosition = world_matrix[1][1]
player_state = testParser.PlayerState(myPosition)


while True:
    pygame.event.get()

    x = player_state.room.x
    y = player_state.room.y
    print(x)
    print(y)
    gameDisplay.fill((255, 255, 255))
    gameDisplay.blit(my_image, [0, 0], [305*x, 305*y, 305, 305])

    pygame.display.update()
    testParser.text_parser(input("Enter command "), player_state)
