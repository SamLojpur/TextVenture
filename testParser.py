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
        talk: The sprite to talk to
    
    Returns:
        Text describing the result of trying to talk with something
"""
def player_talk(_player_state, target):
    # If the player is in the room with the old man
    if _player_state.get_room() == (0, 1):
        # If the player tries to talk to the old man and has killed the goblin
        # the old man tells the player the magic spell
        if target == "old man":
            if _player_state.killedGoblin:
                return "\"Awesome work! the magic word is \'" + MAGIC_SPELL + "\'!\""
            # If the player hasn't yet killed the goblin, the old man shares a
            # hint about how to learn the spell
            else:
                return "\"I'll teach magic to those with the blood of a goblin.\""
        # Is displayed if the user doesn't type a valid target
        else:
            return "You can't talk to that"
    # If the player tries talking to the bunny
    if _player_state.get_room() == (1, 2):
        if target == "bunny":
            return "The bunny can't talk. It is very cute though."
        else:
            return "You can't talk to that"
    # If the player tries talking to the demon
    if _player_state.get_room() == (1, 0):
        if target == "demon":
            return "\"FOOLISH MORTAL. I WILL DESTROY YOUR WORLD. ONLY THE STRONGEST WEAPONS IN THE LAND CAN DEFEAT ME!\""
        else:
            return "You can't talk to that"
    # Is displayed in remaining rooms if the player tries to talk
    else:
        return "There is no one to talk to here."


"""
    Description: Allows the user to take an item
    
    Arguments:
        _player_state: The current state of the player
        item: The item to take
        
    Returns:
        Text describing the result of the user trying to take an object
"""
def player_get(_player_state, item):
    # If the item is a slinlgshot
    if item == "slingshot":
        # If the player doesn't have the slingshot, they take it
        if _player_state.get_room() == (2, 2) and not _player_state.hasSlingshot:
            # Now the player has the slingshot and the sprite is removed
            _player_state.hasSlingshot = True
            _player_state.room.remove_sprite(sprites.Slingshot())
            return "You took the slingshot! Now you can shoot things!"
        else:
            # If the user tries to take a slingshot in an invalid room
            return "There's no slingshot here. "
    # The player tries to take the sword
    elif item == "sword" :
        # If the player doesn't already have the sword
        if _player_state.get_room() == (0, 0) and not _player_state.hasSword:
            # If the sword has been knocked off the cliff, the user can take it
            if _player_state.swordFell == True:
                _player_state.hasSword = True
                _player_state.room.remove_sprite(sprites.Sword())
                return "You took the sword! Now you can attack things!"
            # If the sword hasn't been kncoked off, the user can't take it
            else:
                return "There's a sword but it's too high to reach! If only you could shoot it down."
        # If the user tries to take the sword in an invalid room
        else:
            return "There's no sword here."
    # The user tries to take the shield
    elif item == "shield":
        # If the player doesn't already have the shield
        if _player_state.get_room() == (2, 0) and not _player_state.hasShield:
            # If the player is across the river, they can take the shield
            if _player_state.acrossRiver :
                _player_state.room.remove_sprite(sprites.Shield())
                _player_state.hasShield = True
                return "Woah! You got an awesome shield!"
            # If the player hasn't crossed the river, they can't take the shield
            else:
                _player_state.acrossRiver = True
                return "You need to find a way across the river first!"
        # If the user tries to take a shield from an invalid room
        else:
            return "There's no shield here to take."
    # If the user tries to take something not meant to be taken
    else:
        return "You can't take that."


"""
    Description: Allows the player to use an object
    
    Arguments:
        _player_state: The current state of the player
        arg: The object to use
        
    Returns:
        Text describing the result of using an object
"""
def player_use(_player_state, arg):
    if ' on ' in arg:
        # Splits the argument by the word 'on' if used. ex. use slingshot on x
        x, y = arg.split(' on ')
        # If the object to use is the slingshot
        if x == "slingshot":
            # Perform the same action as shooting
            text = player_shoot(_player_state, y)
            return text
    # If there is no target, inform the user that they need one
    elif arg == 'slingshot':
        return "You need a target to shoot!"
    # If the object does not have a use
    else:
        return "that's not a valid item to use"


"""
    Description: Allows the user to pet the bunny
    
    Arguments:
        _player_state: The current state of the player
        noun: The object to be pet
        
    Returns:
        Text describing the result of tring to pet something
"""
def player_pet(_player_state, noun):
    # If the player pets the bunny
    if noun == "bunny" and _player_state.get_room() == (1, 2):
        return "The bunny nuzzles up to you and purrs!"
    else:
        return "You can't pet that!"
    pass


"""
    Description: Allows the player to shoot a target
    
    Arguments:
        _player_state: The current state of the player
        target: The thing to shoot
    
    Returns:
        Text describing the result of attempting to shoot something
"""
def player_shoot(_player_state, target):
    # If the player has the slingshot
    if _player_state.hasSlingshot:
        # If the player shoots the sword in the appropriate room, it falls
        if target == "sword" and _player_state.get_room() == (0, 0):
            _player_state.swordFell = True
            _player_state.room.remove_sprite(sprites.Sword())
            _player_state.room.add_sprite(sprites.Sword(400, 300))
            return "The sword clatters to your feet"
        # If the player shoots the bunny, it disappears
        elif target == "bunny" and _player_state.get_room() == (1, 2):
            _player_state.room.remove_sprite(sprites.Bunny())
            return "The bunny gets hit and scampers off. You monster."
        # If the player shoots the old man, it runs off
        elif target == "old man" and _player_state.get_room() == (0, 1):
            _player_state.room.remove_sprite(sprites.OldMan())
            return "The man gets hit and scampers off. You monster."
        # If the player shoots the shield, nothing happens
        elif target == "shield" and _player_state.get_room() == (2, 0):
            return "The projectile dings off the shield. It has no effect."
        # If the player shoots the goblin, it is not strong enough to kill him
        elif target == "goblin" and _player_state.get_room() == (0, 2):
            return "It hits the goblin right in the forehead! Oh no! You only made him angrier!"
        # Handles improper targets
        else:
            return "That's not a valid target to shoot"
    # If this player doesn't have the slingshot, they cannot shoot anything
    else:
        return "You have nothing to shoot with"
    pass


"""
    Description: Allows the player to attack a target
    
    Arguments:
        _player_state: The current state of the player
        target: The thing to attack
        
    Returns:
        Text describing the result of attacking something
"""
def player_attack(_player_state, target):
    # If the player has the sword
    if _player_state.hasSword:
        # If the target is the goblin, the goblin is killed
        if target == 'goblin' and _player_state.get_room() == (0, 2):
            _player_state.room.remove_sprite(sprites.Goblin())
            _player_state.killedGoblin = True
            return "You showed no mercy to the goblin and collected its blood."
        # If the target is the demon and the player has obtained the shield, it
        # defeats the demon and the game is over
        if target == 'demon' and _player_state.get_room() == (1, 0) and _player_state.hasShield:
            _player_state.room.remove_sprite(sprites.Boss())
            gameOver = True
            return "You have killed the boss and saved the kingdom!"
        # If the target is the demon and the player has not obtained the shield,
        # it is defeated by the demon and the game is over        
        elif target == 'demon' and _player_state.get_room() == (1, 0) and not(_player_state.hasShield):
            _player_state.room.remove_sprite(sprites.Player())
            _player_state.gameOver = True
            return "Shoot! You were not strong enough to defeat the boss. Game Over!  ..................."
        # If the player tries to attack an invalid target
        else:
            return "You cannot attack that."
    # If the player doesn't have the sword, they cannot attack
    else:
        return "You have nothing to attack with. "

  
"""
    Description: Allows the player to view the description of a room
    
    Arguments:
        _player_state: Current state of the player
        argument: Place holder
        
    Returns:
        Returns the description text for the current room
"""
def player_look(_player_state, argument):
    return _player_state.room.description_text


"""
    Description: Allows the player to get help on learned commands
    
    Arguments:
        _player_state: Current state of the player
        argument: The object that the user needs help with
        
    Returns: Text describing helpful hints about the argument
"""
def player_help(_player_state, argument):
    # Helps the user with each possible command in detail
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
    # Helps the user with general commands
    else:
        return "You can use verbs like 'go', 'take', 'talk', and you can eventually unlock 'shoot' and 'attack'. Type 'help verb' for example commands"


"""
    Parser dictionary that calls specific functions based on the text entered
    by the user.
"""
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


"""
    Description: Checks the input text and runs it through the text parser
    
    Arguments:
        player_state: The current state of the player
        input_string: The text entered by the user
    
    Returns:
        Returns the text generated by the command run
"""
def text_parser(input_string, player_state):
    # Converts input to lowecase and separates it into a verb and a noun via
    # a space
    input_string = input_string.lower()
    verb = input_string.split(' ')[0]
    noun = input_string.partition(' ')[2]
  
    # Doesn't allow the user to enter commands if the game is over
    if player_state.gameOver:
        return "You can't do that when you're dead!."
    else:
        # Calls the appropriate function if the verb is valid        
        if verb in PARSER_DICT:
            output = PARSER_DICT[verb](player_state, noun)
        # If the user enters an unknown command
        else:
            output = """Unknown verb. Try 'help'"""
        
        # Changes the game prompt now that the user has entered a command
        player_state.first_command = False
        # Updates the game screen
        gameUpdate.update_main_screen(player_state)
    return output


"""
    Description: Returns the text that should be displayed on the prompt line
    based on whether or not the user has already entered a command

    Arguments:
        _player_state: The current state of the player
    
    Returns: The text to be displayed on the prompt line
"""
def get_prompt_label(_player_state):
    if _player_state.first_command:
        prompt_label_text = "Enter a command:  "
    else:
        prompt_label_text = "$: "
    return prompt_label_text
