import worldLocations


class PlayerState:
    def __init__(self, room):
        self.room = room
        self.text = ""
        self.first_command = False


def player_move(_player_state, direction):
    _player_state.first_command = True
    current_room = _player_state.room
    _player_state.room = _player_state.room.take_path(direction)
    if _player_state.room.name == current_room.name:
        text = "There is no path that way!"
    else:
        text = "Now entering " + _player_state.room.get_name() + " " + _player_state.room.get_description()

    return text


PARSER_DICT = {
    'go': player_move
}


def text_parser(input_string, player):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
    if verb in PARSER_DICT:
        output = PARSER_DICT[verb](player, noun)

    else:
        output = """Unknown verb. Try 'help'"""

    return output

def prompt_label(_player_state):
    if _player_state.first_command:
        prompt_label_text = "$: "
    else:
        prompt_label_text = "Enter a command:  "
    return prompt_label_text


if __name__ == "__main__":

    world_gen_matrix = [
        [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
        [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
        [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
    ]

    world_matrix = worldLocations.generate_world(world_gen_matrix)
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

