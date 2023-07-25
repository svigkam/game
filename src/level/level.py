import time

from src.level.room import Room


class Level:
    def __init__(self, rooms: [Room], current_room: []):
        self.rooms = rooms
        self.current_room = rooms[current_room[0]][current_room[1]]

        self.checkDoors()

    def checkDoors(self):
        for x in range(len(self.rooms)):
            for y in range(len(self.rooms[x])):
                if isinstance(self.rooms[x][y], Room):
                    if x - 1 > 0 and isinstance(self.rooms[x - 1][y], Room):
                        # TODO: Добавить обьект двери в комнату
                        pass
                    if x + 1 < len(self.rooms) and isinstance(self.rooms[x + 1][y], Room):
                        # TODO: Добавить обьект двери в комнату
                        pass
                    if y - 1 > 0 and isinstance(self.rooms[x][y - 1], Room):
                        # TODO: Добавить обьект двери в комнату
                        pass
                    if y + 1 < len(self.rooms[x]) and isinstance(self.rooms[x][y + 1], Room):
                        # TODO: Добавить обьект двери в комнату
                        pass

    def draw(self):
        self.current_room.draw()
