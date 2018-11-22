

def player_move(direction):
    # a test function to prove this works
    print("I went " + direction)


parser_dict = {
    'go': player_move
}


def text_parser(input_string):
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]

    parser_dict[verb](noun)

    return verb


if __name__ == "__main__":
    text_parser("Go South")
    text_parser("Go East")
    text_parser("Go West")
    text_parser("GO north")
    text_parser("go to yo momma's house")