import worldLocations


class PlayerState:
    def __init__(self, room):
        self.room = room


def player_move(player_state, direction):

    player_state.room = player_state.room.take_path(direction)


PARSER_DICT = {
    'go': player_move
}


def text_parser(input_string, player):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
    if verb in PARSER_DICT:
        PARSER_DICT[verb](player, noun)

    else:
        print("Uh oh! I don't recognize that word!")
        print("Type help for examples of words you can use")


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

