import worldLocations
import gameUpdate
import sprites
MAGIC_SPELL = "cast"



def player_cast(_player_state, _):
    if _player_state.get_room() == (2, 0):
        return "Woah! The magic of " + MAGIC_SPELL + " let you jump over the river!"

    else:
        _player_state.acrossRiver = not _player_state.acrossRiver
        return "Woah! The magic of " + MAGIC_SPELL + " let you jump!"


def player_move(_player_state, direction):

    current_room = _player_state.room
    _player_state.room = _player_state.room.take_path(direction)
    if _player_state.room.name == current_room.name:
        text = "There is no path that way!"
    elif _player_state.acrossRiver:
        return "You need to find a way across the river first!"
    else:
        text = "Now entering " + _player_state.room.get_name() + "\n" + _player_state.room.get_description()

    return text


def player_talk(_player_state, target):
    if _player_state.get_room() == (0, 1):
        return "\"Oh if only I could get my treasure from the north. It's guarded by a troll though :(\""
    if _player_state.get_room() == (1, 2):
        return "The bunny can't talk. It is very cute though. I need to fill another line"
    else:
        return "There is no one to talk to here."


def player_get(_player_state, item):

    if item == "slingshot":
        if _player_state.get_room() == (2, 2):
            _player_state.hasSlingshot = True
            return "You took the slingshot! Now you can shoot things!"
    elif item == "sword" and not _player_state.hasSword:
        if _player_state.get_room() == (0, 2):
            if _player_state.swordFell == True:
                _player_state.hasSword = True
                return "You took the sword! Now you can attack things!"
            else:
                return "There's a sword but it's too high to reach! If only you could shoot it down"
    elif item == "upgrade":
        if _player_state.get_room() == (2, 0):
            if _player_state.acrossRiver == True:
                return "Woah! You got an awesome shield!"
            else:
                return "You need to find a way across the river first!"
    else:
        return "There's nothing here to take!"

    pass


def player_use(_player_state, arg):
    x, y = arg.split(' on ')
    if x == "slingshot":
        player_shoot(_player_state, y)

    return "that's not a valid item to use"

def player_pet(_player_state, noun):
    if noun == "bunny":
        return "The bunny nuzzles up to you and purrs!"
    else:
        return "You can't pet that!"
    pass


def player_shoot(_player_state, target):
    if target == "sword" and _player_state.get_room() == (0, 2):
        _player_state.swordFell = True
        return "The you fire the slingshot and the sword clatters to your feet"
    elif target == "bunny" and _player_state.get_room() == (1, 2):
        _player_state.room.remove_all_sprites()
        _player_state.room.add_sprite(sprites.Player(200, 200))
        return "The bunny gets hit and scampers off. You monster."
    elif target == "wizard" and _player_state.get_room() == (0, 1):
        return "The man gets hit and scampers off. You monster."
    else:
        return "That's not a valid target to shoot"
    pass


def player_help(_player_state, argument):
    return "Here are the words we have so far!: go, talk, cast, use and shoot"

PARSER_DICT = {
    'go'    : player_move,
    'talk'  : player_talk,
    'take'  : player_get,
    'use'   : player_use,
    'pet'   : player_pet,
    'shoot' : player_shoot,
    MAGIC_SPELL: player_cast,


}


def text_parser(input_string, player_state):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
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

