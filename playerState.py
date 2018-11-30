

class PlayerState:
    def __init__(self, room):
        self.gameDisplay = None
        self.room = room
        self.text = ""
        self.first_command = True
        self.acrossRiver = False
        self.hasSlingshot = False
        self.swordFell = False
        self.hasSword = False

    def get_room(self):
        return self.room.x, self.room.y

