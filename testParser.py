import worldLocations
MAGIC_SPELL = "cast"


class PlayerState:
    def __init__(self, room):
        self.room = room
        self.text = ""
        self.first_command = True


def player_cast(_player_state, direction):
    if _player_state.room.x == 2 and _player_state.room.y == 0:
        return "Woah! The magic of " + MAGIC_SPELL + " let you jump over the river!"
    else:
        return "Woah! The magic of " + MAGIC_SPELL + " let you jump!"


def player_move(_player_state, direction):

    current_room = _player_state.room
    _player_state.room = _player_state.room.take_path(direction)
    if _player_state.room.name == current_room.name:
        text = "There is no path that way!"
    else:
        text = "Now entering " + _player_state.room.get_name() + " " + _player_state.room.get_description()

    return text


def player_talk (_player_state, words):
    pass


def player_get (_player_state, item):
    pass


def player_use (_player_state, item):
    pass


def player_pet (_player_state, noun):
    pass


def player_shoot (_player_state, words):
    pass


PARSER_DICT = {
    'go'    : player_move,
    'talk'  : player_talk,
    'grab'  : player_get,
    'use'   : player_use,
    'pet'   : player_pet,
    'shoot ': player_shoot,
    MAGIC_SPELL: player_cast,


}


def text_parser(input_string, player):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
    if verb in PARSER_DICT:
        output = PARSER_DICT[verb](player, noun)

    else:
        output = """Unknown verb. Try 'help'"""

    player.first_command = False

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

