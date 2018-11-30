#import testParser
import pygame
import sprites
import playerState

def generate_world():
    world_gen_matrix = [
        [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
        [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
        [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
    ]

    world = worldgen_from_matrix(world_gen_matrix)
    world[0][0].remove_path_to(world[0][1])
    world[0][1].remove_path_to(world[0][0])

    world[0][2].remove_path_to(world[0][1])
    world[0][1].remove_path_to(world[0][2])


    player_sprite = sprites.Player(200,200)
    for row in world:
        for room in row:
            room.add_sprite(player_sprite)

    world[1][0].add_sprite(sprites.OldMan())
    world[0][0].add_sprite(sprites.Sword())
    world[2][1].add_sprite(sprites.Bunny())

    print(world[1][1].name)

    myPosition = world[1][1]

    player_state = playerState.PlayerState(myPosition)
    return player_state


def worldgen_from_matrix(world_array):
    output_array = []
    for y, i in enumerate(world_array):
        current_row = []
        output_array.append(current_row)
        for x, j in enumerate(i):
            current_room = Room(*j, x, y)
            current_row.append(current_room)

    for i in range(len(output_array)):
        for j in range(len(output_array[0])):
            current_room = output_array[i][j]
            if i - 1 >= 0:
                north_room = output_array[i-1][j]
                current_room.add_path('north', north_room)
            if i + 1 < len(output_array):
                south_room = output_array[i+1][j]
                current_room.add_path('south', south_room)
            if j - 1 >= 0:
                west_room = output_array[i][j-1]
                current_room.add_path('west', west_room)
            if j + 1 < len(output_array[0]):
                east_room = output_array[i][j+1]
                current_room.add_path('east', east_room)

    return output_array




class Room:

    def __init__(self, name="Unknown Location", description_text="No Description", x=0, y=0):
        self.x = x
        self.y = y
        self.paths = {
        }
        self.description_text = description_text
        self.name = name
        self.text = ""
        self.all_sprites = pygame.sprite.Group()

    def add_path(self, direction, room):
            if isinstance(room, Room):
                self.paths[direction] = room
            else:
                pass
                print(type(room))

    def remove_path_to(self, room):
        self.paths = {k: v for k, v in self.paths.items() if v != room}

    def take_path(self, direction):
        if direction in self.paths:
            print("Now entering " + self.paths[direction].name + self.paths[direction].description_text)
            return self.paths[direction]
        else:
            print("There is no path that way!")
            return self
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description_text

    def add_sprite(self, sprite):
        self.all_sprites.add(sprite)

    def get_sprites(self):
        return self.all_sprites

    def remove_all_sprites(self):
        self.all_sprites.empty()

    # def render_room(self):
    #     all_sprites = pygame.sprite.Group()
    #     #player_sprite = sprites.Player(200, 200)
    #     #all_sprites.add(player_sprite)
    #     # Room 8:
    #     if self.x == 1 and self.y == 2:
    #         player_sprite = sprites.Player(200, 125)
    #         bunny_sprite = sprites.Bunny()
    #         all_sprites.add(bunny_sprite)
    #     # Room 4:
    #     elif self.x == 0 and self.y == 1:
    #         player_sprite = sprites.Player(200, 200)
    #         oldMan_sprite = sprites.OldMan()
    #         all_sprites.add(oldMan_sprite)
    #
    #     # Room 1:
    #     elif self.x == 0 and self.y == 0:
    #         player_sprite = sprites.Player(300, 350)
    #         sword_sprite = sprites.Sword()
    #         all_sprites.add(sword_sprite)
    #
    #     else:
    #         player_sprite = sprites.Player(200, 200)
    #
    #
    #     all_sprites.add(player_sprite)
    #     return all_sprites

            
    # @todo render the sprites for the room here


if __name__ == "__main__":

    world_gen_matrix = [
        [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
        [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
        [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
    ]

    world_matrix = worldgen_from_matrix(world_gen_matrix)
    print(world_matrix[1][1].name)

    myPosition = world_matrix[1][1]

    myPosition = myPosition.take_path('East')
    myPosition = myPosition.take_path('East')
    myPosition = myPosition.take_path('South')
    myPosition = myPosition.take_path('West')


