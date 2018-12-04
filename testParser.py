import worldLocations
import gameUpdate
import sprites
MAGIC_SPELL = "finances"


def player_cast(_player_state, _):
    if _player_state.get_room() == (2, 0):
        _player_state.acrossRiver = not _player_state.acrossRiver
        _player_state.room.remove_sprite(sprites.Player())
        if _player_state.acrossRiver:
            _player_state.room.add_sprite(sprites.Player(200, 5))
        else:
            _player_state.room.add_sprite(sprites.Player(200, 400))

        return "The magic of " + MAGIC_SPELL + " let you jump over the river!"
    else:
        return "The magic of " + MAGIC_SPELL + " let you jump!"


def player_move(_player_state, direction):

    current_room = _player_state.room

    _player_state.room = _player_state.room.take_path(direction)

    if _player_state.get_room() == (0, 1):
        _player_state.room.add_sprite(sprites.OldMan())

    if _player_state.room.name == current_room.name:
        if _player_state.get_room() == (0, 1) and direction == "house":
            text = "You can't enter someone else's house!"
        else:
            text = "There is no path that way!"
    elif _player_state.acrossRiver:
        _player_state.room = current_room
        return "You need to find a way across the river first!"
    else:
        if _player_state.visited_room():
            text = "Now entering " + _player_state.room.get_name()
        else:
            text = "Now entering " + _player_state.room.get_name() +  ": " + _player_state.room.get_description()

    return text


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
        if _player_state.get_room() == (2, 2):
            _player_state.hasSlingshot = True
            _player_state.room.remove_sprite(sprites.Slingshot())
            return "You took the slingshot! Now you can shoot things!"
        else:
            return "There's no slingshot here. "
    elif item == "sword" and not _player_state.hasSword:
        if _player_state.get_room() == (0, 0):
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
        if _player_state.get_room() == (2, 0):
            if _player_state.acrossRiver == True:
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
    # 'use slingshot' causes bug
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
        elif target == "shield":
            return "The projectile dings off the shield. It has no effect."
        elif target == "goblin":
            return "It hits the goblin right in the forehead! Oh no! You only made him angrier!"
        else:
            return "That's not a valid target to shoot"
    else:
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
        if target == 'boss' and _player_state.get_room() == (1, 0) and _player_state.hasShield:
            _player_state.room.remove_sprite(sprites.Boss())
            gameOver = True
            return "You have killed the boss and saved the kingdom!"
        elif target == 'boss' and _player_state.get_room() == (1, 0) and not(_player_state.hasShield):
            _player_state.room.remove_sprite(sprites.Player())
            _player_state.gameOver = True
            return "You were not strong enough to defeat the boss. "
        else:
            return "You cannot attack that."
    else:
        return "You have nothing to attack with. "
        


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
        return "You can use verbs like 'go', 'take', 'talk', and you can eventually unlock 'shoot' and 'attack'. Type help 'verb' for example commands"


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

