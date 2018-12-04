#import testParser
import pygame
import sprites
import playerState


def generate_world():
    world_gen_matrix = [
        [['the Cliffs', 'Above you, a sword lies on top of a cliff. It seems like it would fall if you shot it somehow. To the south is the Cabin.'], ['the Castle', 'Before you stands an emo kid, usin\' some dark magics on the kingdom. You must stop him!'], ['the River', 'Across the river lies a powerful shield. The river is running too fast to cross.']],
        [['the Lone Cabin', 'The old man in front of you looks magical. Maybe you could talk to him.'], ['the Plains', 'The fifth place'], ['the Path', 'You stand at a crossroads. To the north is the river; to the south is the forest.']],
        [['the Grove', 'A vicious goblin roams this area. You would need a powerful sword to kill him.'], ['the Forest', 'A very cute bunny is here, his fur is so fluffy you can\'t stand it'], ['the Forest (east)', 'There is a slingshot sitting on the ground before you. You should take it.']],
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
    # the x and the y are backwards here be careful ron
    world[0][2].remove_sprite(sprites.Player())
    world[0][2].add_sprite(sprites.Player(200, 400))
    world[0][2].add_sprite(sprites.Shield())

    world[1][0].add_sprite(sprites.OldMan())
    world[0][0].add_sprite(sprites.Sword())
    world[2][1].add_sprite(sprites.Bunny())
    world[2][2].add_sprite(sprites.Slingshot())
    world[2][0].add_sprite(sprites.Goblin())
    world[0][1].add_sprite(sprites.Boss())

    my_position = world[1][1]

    player_state = playerState.PlayerState(my_position)
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
        for j in range(len(output_array[i])):
            current_room = output_array[i][j]
            if i - 1 >= 0:
                north_room = output_array[i-1][j]
                current_room.add_path('north', north_room)
                current_room.add_path('up', north_room)
                current_room.add_path('n', north_room)
            if i + 1 < len(output_array):
                south_room = output_array[i+1][j]
                current_room.add_path('south', south_room)
                current_room.add_path('down', south_room)
                current_room.add_path('s', south_room)
            if j - 1 >= 0:
                west_room = output_array[i][j-1]
                current_room.add_path('west', west_room)
                current_room.add_path('left', west_room)
                current_room.add_path('w', west_room)
            if j + 1 < len(output_array[0]):
                east_room = output_array[i][j+1]
                current_room.add_path('east', east_room)
                current_room.add_path('e', east_room)
                current_room.add_path('right', east_room)

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
        self.sprites_list = []
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
        #print(type(sprite))
        self.sprites_list.append(sprite)
        self.sprite_update()

    def get_sprites(self):
        return self.all_sprites

    def remove_sprite(self, sprite):
        self.sprites_list = [x for x in self.sprites_list if not (type(sprite) == type(x))]
        self.sprite_update()

    def sprite_update(self):
        self.all_sprites.empty()
        for sprite in self.sprites_list:
            self.all_sprites.add(sprite)


            
    # @todo render the sprites for the room here


