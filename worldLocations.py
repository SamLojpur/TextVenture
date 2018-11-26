
def generate_world(world_array):
    output_array = []
    for y, i in enumerate(world_array):
        current_row = []
        output_array.append(current_row)
        for x, j in enumerate(i):
            current_room = Room(*j, x, y)
            current_row.append(current_room)

    for i in range(len(output_array)):
        for j in range(len(output_array[0])):
            current_room = output_array[i][j]
            if i - 1 >= 0:
                north_room = output_array[i-1][j]
                current_room.add_path('north', north_room)
            if i + 1 < len(output_array):
                south_room = output_array[i+1][j]
                current_room.add_path('south', south_room)
            if j - 1 >= 0:
                west_room = output_array[i][j-1]
                current_room.add_path('west', west_room)
            if j + 1 < len(output_array[0]):
                east_room = output_array[i][j+1]
                current_room.add_path('east', east_room)

    return output_array




class Room:

    def __init__(self, name="Unknown Location", description_text="No Description", x=0, y=0):
        self.x = x
        self.y = y
        self.paths = {
        }
        self.description_text = description_text
        self.name = name
        self.text = ""
    # @todo removepathto(room we could go to)
    def add_path(self, direction, room):
            if isinstance(room, Room):
                self.paths[direction] = room
            else:
                pass
                print(type(room))

    def take_path(self, direction):
        if direction in self.paths:
            print("Now entering " + self.paths[direction].name)
            return self.paths[direction]
        else:
            print("There is no path that way!")
            return self
        
    def get_name(self):
        print("HI", self.name)
        return self.name

    def render_room(self, sprite):
        pass
    # @todo render the sprites for the room here


if __name__ == "__main__":

    world_gen_matrix = [
        [['Place 1', 'The first place'], ['Place 2', 'The second place'], ['Place 3', 'The third place']],
        [['Place 4', 'The fourth place'], ['Place 5', 'The fifth place'], ['Place 6', 'The sixth place']],
        [['Place 7', 'The seventh place'], ['Place 8', 'The eighth place'], ['Place 9', 'The ninth place']],
    ]

    world_matrix = generate_world(world_gen_matrix)
    print(world_matrix[1][1].name)

    myPosition = world_matrix[1][1]

    myPosition = myPosition.take_path('East')
    myPosition = myPosition.take_path('East')
    myPosition = myPosition.take_path('South')
    myPosition = myPosition.take_path('West')


