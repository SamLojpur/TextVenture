

class PlayerState:
    def __init__(self, room):
        self.gameDisplay = None
        self.room = room
        self.text = ""
        self.first_command = True
        self.acrossRiver = False
        self.hasSlingshot = False
        self.swordFell = False
        self.hasSword = True
        self.hasShield = False
        self.gameOver = False
        self.killedGoblin = False
        self.hasVisited = [[False, False, False], [False, False, False], [False, False, False]]

    def get_room(self):
        return self.room.x, self.room.y

    def visited_room(self):

        if self.hasVisited[self.room.x][self.room.y]:
            return True
        else:
            self.hasVisited[self.room.x][self.room.y] = True
            return False

