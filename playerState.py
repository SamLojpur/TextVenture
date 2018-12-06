"""
    Description: PlayerState describes all of the attributes of the player
    allowing us to track the user's progress in the game

    Arguments:
        room: Describes the room that the player starts in

    Returns:
        None
"""


class PlayerState:

    def __init__(self, room):
        # Each member is a flag that represents an aspect of the player's
        # progress
        self.gameDisplay = None
        self.room = room
        self.text = ""
        self.first_command = True
        self.acrossRiver = False
        self.hasSlingshot = False
        self.swordFell = False
        self.hasSword = False
        self.hasShield = False
        self.gameOver = False
        self.killedGoblin = False
        self.hasVisited = [[False, False, False], [False, False, False],
                           [False, False, False]]

    # Returns the room that the player is in
    def get_room(self):
        return self.room.x, self.room.y

    """
        Description: Returns a boolean value describing whether or not the
        player has previously visited the room that they are in

        Arguments:
            None

        Returns:
            True if the player has previously visited the current room that
            they are in, False if not
    """
    def visited_room(self):
        if self.hasVisited[self.room.x][self.room.y]:
            return True
        else:
            self.hasVisited[self.room.x][self.room.y] = True
            return False
