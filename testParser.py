import worldLocations
import gameUpdate
import sprites
MAGIC_SPELL = "finances"


"""
    Description: Handles the event when the player uses the magic spell
    
    Arguments:
        player_cast(_player_state): The current state of the player
        _: A place holder
    
    Returns:
        Lets the player jump over the river if in the appropriate room and
        informs the user that they have the ability to jump if not in the
        appropriate room
"""
def player_cast(_player_state, _):
    # Crosses the player over the river if in the correct room
    if _player_state.get_room() == (2, 0):
        # After the player crosses the river, their position is updated
        _player_state.acrossRiver = not _player_state.acrossRiver
        _player_state.room.remove_sprite(sprites.Player())
        # Moves the sprite of the player depending on which side of the river
        # they are on
        if _player_state.acrossRiver:
            _player_state.room.add_sprite(sprites.Player(200, 5))
        else:
            _player_state.room.add_sprite(sprites.Player(200, 400))
        # Returns text explaining that the character has crossed the river
        return "The magic of " + MAGIC_SPELL + " let you jump over the river!"
    # If user is not in the room with the river
    else:
        # Informs the user that they gained the ability to jump
        return "The magic of " + MAGIC_SPELL + " let you jump!"


"""
    Description:
"""
def player_move(_player_state, direction):
    # Retrieves the current room of the player
    current_room = _player_state.room
    _player_state.room = _player_state.room.take_path(direction)

    # Re-adds the oldman sprite if he was previously attacked
    if _player_state.get_room() == (0, 1):
        _player_state.room.add_sprite(sprites.OldMan())

    # Checks if the entered direction leads to a valid path
    if _player_state.room.name == current_room.name:
        # If the user tries to enter the house in the room with the old man
        if _player_state.get_room() == (0, 1) and direction == "house":
            text = "You can't enter someone else's house!"
        # If the user enters an invalid path
        else:
            text = "There is no path that way!"
    # If the user is across the river they must cross back before leaving the
    # room
    elif _player_state.acrossRiver:
        _player_state.room = current_room
        return "You need to find a way across the river first!"
    # Only displays the description text for rooms that have not yet been
    # explored
    else:
        if _player_state.visited_room():
            text = "Now entering " + _player_state.room.get_name()
        else:
            text = "Now entering " + _player_state.room.get_name() +  ": " + _player_state.room.get_description()

    return text


"""
    Allows the player to talk to characters in the game

    Arguments:
    
"""
def player_talk(_player_state, target):
    if _player_state.get_room() == (0, 1):
        if target == "old man":
            if _player_state.killedGoblin:
                return "\"Awesome work! the magic word is \'" + MAGIC_SPELL + "\'!\""
            else:
                return "\"I'll teach magic to those with the blood of a goblin.\""
        else:
            return "You can't talk to that"
    if _player_state.get_room() == (1, 2):
        if target == "bunny":
            return "The bunny can't talk. It is very cute though."
        else:
            return "You can't talk to that"

    if _player_state.get_room() == (1, 0):
        if target == "demon":
            return "\"FOOLISH MORTAL. I WILL DESTROY YOUR WORLD. ONLY THE STRONGEST WEAPONS IN THE LAND CAN DEFEAT ME!\""
        else:
            return "You can't talk to that"


    else:
        return "There is no one to talk to here."


def player_get(_player_state, item):

    if item == "slingshot":

        if _player_state.get_room() == (2, 2) and not _player_state.hasSlingshot:
            _player_state.hasSlingshot = True
            _player_state.room.remove_sprite(sprites.Slingshot())
            return "You took the slingshot! Now you can shoot things!"
        else:
            return "There's no slingshot here. "
    elif item == "sword" :
        if _player_state.get_room() == (0, 0) and not _player_state.hasSword:
            if _player_state.swordFell == True:
                _player_state.hasSword = True
                _player_state.room.remove_sprite(sprites.Sword())
                return "You took the sword! Now you can attack things!"
            else:
                #return "The sword is too high!"
                return "There's a sword but it's too high to reach! If only you could shoot it down"
        else:
            return "There's no sword here."
    elif item == "shield":
        if _player_state.get_room() == (2, 0) and not _player_state.hasShield:
            if _player_state.acrossRiver :
                _player_state.room.remove_sprite(sprites.Shield())
                _player_state.hasShield = True
                return "Woah! You got an awesome shield!"
            else:
                _player_state.acrossRiver = True
                return "You need to find a way across the river first!"
        else:
            return "There's no shield here to take."
    else:
        return "There's no " + item + " here to take."

    pass


def player_use(_player_state, arg):
    # 'use slingshot' causes bug\
    #print("ARG", arg)
    if ' on ' in arg:
        #print("ARG", arg)
        x, y = arg.split(' on ')
        if x == "slingshot":
            print("Slingshot")
            text = player_shoot(_player_state, y)
            return text
    elif arg == 'slingshot':
        return "You need a target to shoot!"
    else:
        return "that's not a valid item to use"

def player_pet(_player_state, noun):
    if noun == "bunny" and _player_state.get_room() == (1, 2):
        return "The bunny nuzzles up to you and purrs!"
    else:
        return "You can't pet that!"
    pass


def player_shoot(_player_state, target):
    print("PLAYER SHOOT")
    if _player_state.hasSlingshot:
        if target == "sword" and _player_state.get_room() == (0, 0):
            _player_state.swordFell = True
            _player_state.room.remove_sprite(sprites.Sword())
            _player_state.room.add_sprite(sprites.Sword(400, 300))
            return "The sword clatters to your feet"
        elif target == "bunny" and _player_state.get_room() == (1, 2):
            _player_state.room.remove_sprite(sprites.Bunny())
            return "The bunny gets hit and scampers off. You monster."
        elif target == "old man" and _player_state.get_room() == (0, 1):
            _player_state.room.remove_sprite(sprites.OldMan())
            return "The man gets hit and scampers off. You monster."
        elif target == "shield" and _player_state.get_room() == (2, 0):
            return "The projectile dings off the shield. It has no effect."
        elif target == "goblin" and _player_state.get_room() == (0, 2):
            return "It hits the goblin right in the forehead! Oh no! You only made him angrier!"
        else:
            return "That's not a valid target to shoot"
    else:
        print("NOTHING TO SHOOT")
        return "You have nothing to shoot with"
    pass
# add boss
# fix old man spell
def player_attack(_player_state, target):
    if _player_state.hasSword:
        # Room 2
        if target == 'goblin' and _player_state.get_room() == (0, 2):
            _player_state.room.remove_sprite(sprites.Goblin())
            _player_state.killedGoblin = True
            return "You showed no mercy to the goblin and collected its blood."
        if target == 'demon' and _player_state.get_room() == (1, 0) and _player_state.hasShield:
            _player_state.room.remove_sprite(sprites.Boss())
            gameOver = True
            return "You have killed the boss and saved the kingdom!"
        elif target == 'demon' and _player_state.get_room() == (1, 0) and not(_player_state.hasShield):
            _player_state.room.remove_sprite(sprites.Player())
            _player_state.gameOver = True
            return "Shoot! You were not strong enough to defeat the boss. Game Over!  ..................."
        else:
            return "You cannot attack that."
    else:
        return "You have nothing to attack with. "
        
def player_look(_player_state, argument):
    #@todo if you took something dont describe it
    return _player_state.room.description_text

def player_help(_player_state, argument):
    if argument == "go":
        return "You can type 'go west' 'go left' or 'go w'. All of these will move you one screen to the left."
    if argument == "take":
        return "You can type 'take slingshot' to take a slingshot from off the ground."
    if argument == "talk":
        return "You can type 'talk old man' to speak with an old man."
    if argument == "shoot":
        return "You can type 'shoot sword' to shoot at a sword if you have a slingshot."
    if argument == "attack":
        return "You can type 'attack goblin' to attack a goblin if you have a sword."
    if argument == "help":
        return "You know what help does."
    else:
        return "You can use verbs like 'go', 'take', 'talk', and you can eventually unlock 'shoot' and 'attack'. Type 'help verb' for example commands"





PARSER_DICT = {
    'help'  : player_help,
    'move'  : player_move,
    'cast'  : player_cast,
    'go'    : player_move,
    'talk'  : player_talk,
    'take'  : player_get,
    'get'   : player_get,
    'use'   : player_use,
    'pet'   : player_pet,
    'shoot' : player_shoot,
    'attack': player_attack,
    'hit'   : player_attack,
    'kill'  : player_attack,
    'look'  : player_look,
    MAGIC_SPELL: player_cast,


}


def text_parser(input_string, player_state):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
    if player_state.gameOver:
        return "You can't do that when you're dead!."
    else:
        if verb in PARSER_DICT:
            output = PARSER_DICT[verb](player_state, noun)

        else:
            output = """Unknown verb. Try 'help'"""

        player_state.first_command = False
        gameUpdate.update_main_screen(player_state)
    return output


def get_prompt_label(_player_state):
    if _player_state.first_command:
        prompt_label_text = "Enter a command:  "
    else:
        prompt_label_text = "$: "
    return prompt_label_text


if __name__ == "__main__":

    world_gen_matrix = [
        [['the Cliffs', 'The first place'], ['the Castle', 'The second place'], ['the River', 'The third place']],
        [['the Lone Cabin', 'The fourth place'], ['the Plains', 'The fifth place'], ['the Path', 'The sixth place']],
        [['the Grove', 'The seventh place'], ['the Forest', 'The eighth place'], ['the Forest (east)', 'The ninth place']],
    ]

    world_matrix = worldLocations.worldgen_from_matrix(world_gen_matrix)
    print(world_matrix[1][1].name)

    myPosition = world_matrix[1][1]
    player_state = myPosition

    # text_parser("Go South")
    # text_parser("Go East")
    # text_parser("Go West")
    # text_parser("GO north")
    # text_parser("go to yo momma's house")

    while True:
        text_parser(input("Enter command "), player_state)

