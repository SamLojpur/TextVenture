#import testParser
import pygame
import sprites
import playerState

"""
    Description: Generates a new world or array of rooms. Basically starts the game

    Arguments:
        None

    Returns:
        playerstate (PlayerState): the saved gamedata object for this game.
"""
def generate_world():
    # this matrix is responsible for generating the world and the descriptions for the whole world. The matrix can be
    # a square array of any size, but this one fits the map
    world_gen_matrix = [
        [['the Cliffs', 'Above you, a sword lies on top of a cliff. It seems like it would fall if you shot it somehow. To the south is the Cabin.'], ['the Castle', 'Before you stands a demon, usin\' some dark magics on the kingdom. You must stop him!'], ['the River', 'Across the river lies a powerful shield. The river is running too fast to cross.']],
        [['the Lone Cabin', 'The old man in front of you looks magical. Maybe you could talk to him.'], ['the Plains', 'The least interesting spot. The demon lies north of here.'], ['the Path', 'You stand at a crossroads. To the north is the river; to the south is the forest.']],
        [['the Grove', 'A vicious goblin roams this area. You would need a powerful sword to kill him.'], ['the Forest', 'A very cute bunny is here, his fur is so fluffy you can\'t stand it'], ['the Forest (east)', 'There is a slingshot sitting on the ground before you. You should take it.']],
    ]

    # make a world (2d array of rooms) from the worldgen Matrix
    world = worldgen_from_matrix(world_gen_matrix)

    # the x and the y are backwards here be careful ron
    # remove paths between places that should not have paths
    world[0][0].remove_path_to(world[0][1])
    world[0][1].remove_path_to(world[0][0])
    world[0][2].remove_path_to(world[0][1])
    world[0][1].remove_path_to(world[0][2])

    #  add the player sprite to every room
    player_sprite = sprites.Player(200, 200)
    for row in world:
        for room in row:
            room.add_sprite(player_sprite)
    # add sprites and remove sprites from various specific rooms.
    world[0][2].remove_sprite(sprites.Player())
    world[0][2].add_sprite(sprites.Player(200, 400))
    world[0][2].add_sprite(sprites.Shield())
    world[1][0].add_sprite(sprites.OldMan())
    world[0][0].add_sprite(sprites.Sword())
    world[2][1].add_sprite(sprites.Bunny())
    world[2][2].add_sprite(sprites.Slingshot())
    world[2][0].add_sprite(sprites.Goblin())
    world[0][1].add_sprite(sprites.Boss())

    # choose the center room as myposition
    my_position = world[1][1]

    # create a playerstate object for holding all gamedata, and return it for this world.
    player_state = playerState.PlayerState(my_position)
    return player_state

"""
    Description: creates a 2d array of connected room objects from a 2d array of strings
    for names and descriptions.

    Arguments:
        world_array (Triple nseted array of strings): The input for the name and descriptions of all rooms

    Returns:
        output_array (Room[][]): 2d array of rooms that composes the rooms.
"""
def worldgen_from_matrix(world_array):
    output_array = []
    # Make an array of rooms the size of the original array
    for y, i in enumerate(world_array):
        current_row = []
        output_array.append(current_row)
        for x, j in enumerate(i):
            current_room = Room(*j, x, y)
            current_row.append(current_room)

    # Connect all the rooms to other rooms.
    for i in range(len(output_array)):
        for j in range(len(output_array[i])):
            current_room = output_array[i][j]
            if i - 1 >= 0:
                north_room = output_array[i-1][j]
                # Add north, up and n as valid paths to follow to go up
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

"""
    Description: Makes a room object that controls what to display and where to go from the room

    Arguments:
        name (string): Name of the room to display
        description text (string): Description to display when first entering the room
        x (int): X coordinate of the room
        y (int): Y coordinate of the room
"""
class Room:
    # just inits the variables
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

    """
        Description: add a path in a direction, to the path dictionary.

        Arguments:
            direction (string): the string that will take the player in this direction
            room: Describes the room to go to

        Returns:
            None
    """
    def add_path(self, direction, room):
            if isinstance(room, Room):
                # just stick him in a dictionary
                self.paths[direction] = room

    """
        Description: remove all paths to a room from the path dictionary

        Arguments:
            room: The room object to remove from the dict

        Returns:
            None
    """
    def remove_path_to(self, room):
        # remove all paths to a room from the path dictionary
        self.paths = {k: v for k, v in self.paths.items() if v != room}

    """
        Description: takes a path and returns the destination of that path, or the same room if no path exists
        Arguments:
            direction (string): the direction the player wants to go

        Returns:
            room: The room object that direction points to
    """
    def take_path(self, direction):
        # if the path had an entry for direction
        if direction in self.paths:

            # then take that path and return the destination
            return self.paths[direction]
        else:
            # otherwise return this room
            return self

    def get_name(self):
        # obvious name getter
        return self.name
    
    def get_description(self):
        # obvious desc getter
        return self.description_text

    """
        Description: takes a sprite and adds it to the spritelist
        Arguments:
            sprite: the sprite object that you should display in this room

        Returns:
            None
    """
    def add_sprite(self, sprite):
        # add a sprite to the list of sprites to show in this room
        self.sprites_list.append(sprite)
        # then update the spritegroup
        self.sprite_update()

    """
        Description: returns the spritegroup object for this room
        Arguments:
            None
        Returns:
            allsprites: the spritegroup of sprites in this room
    """
    def get_sprites(self):
        # return the list of sprites to display here
        return self.all_sprites

    """
        Description: remove a sprite from the spritelist
        Arguments:
            sprite: a sprite of the same type as the one you want to remove

        Returns:
            None
    """
    def remove_sprite(self, sprite):
        # because its hard to remove an individual sprite from a spritegroup
        # we make a list of sprites and check if a sprite is of the same type as the
        # one we pass here to remove it.
        # So we just generate a new sprite of the same type and check this list for matches
        # and remove them from the OG list
        self.sprites_list = [x for x in self.sprites_list if not (type(sprite) == type(x))]
        # then update the spritegroup
        self.sprite_update()

    """
        Description: update the spritelist from the list of sprites 
        Arguments:
            None

        Returns:
            None
    """
    def sprite_update(self):
        # anytime we change the list, delete the spritegroup and add a new one with the updated list
        # this is because displaying spritegroups is easy, but removing one specific sprite from one is
        # impossible unless you know the sprite object you want to remove
        # remove all sprites from the spritegroup
        self.all_sprites.empty()
        # add all the sprites in the list to the spritegroup
        for sprite in self.sprites_list:
            self.all_sprites.add(sprite)
