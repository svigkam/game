import time

from src.config import TILE_SIZE
from src.level.level_config import FloorsTypes, DoorsCoords
from src.level.room import Room, loadImage
from src.objects.door import Door


class Level:
    def __init__(self, rooms: [Room], current_room: []):
        self.rooms = rooms
        self.current_room_coords = current_room
        self.current_room = rooms[current_room[0]][current_room[1]]
        self.level_type = FloorsTypes.BASEMENT

        self.checkDoors()

        self.current_room.player.collideObjects = self.current_room.objects

    def checkDoors(self):
        for x in range(len(self.rooms)):
            for y in range(len(self.rooms[x])):
                if isinstance(self.rooms[x][y], Room):
                    if x - 1 > -1 and isinstance(self.rooms[x - 1][y], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.LEFT.value[0] * TILE_SIZE, DoorsCoords.LEFT.value[1] * TILE_SIZE,
                                 loadImage(self.level_type.value, -1), DoorsCoords.LEFT.value[2],
                                 DoorsCoords.LEFT.name))
                    if x + 1 < len(self.rooms) and isinstance(self.rooms[x + 1][y], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.RIGHT.value[0] * TILE_SIZE, DoorsCoords.RIGHT.value[1] * TILE_SIZE,
                                 loadImage(self.level_type.value, -1), DoorsCoords.RIGHT.value[2],
                                 DoorsCoords.RIGHT.name))
                    if y - 1 > -1 and isinstance(self.rooms[x][y - 1], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.UP.value[0] * TILE_SIZE, DoorsCoords.UP.value[1] * TILE_SIZE,
                                 loadImage(self.level_type.value, -1), DoorsCoords.UP.value[2], DoorsCoords.UP.name))
                    if y + 1 < len(self.rooms[x]) and isinstance(self.rooms[x][y + 1], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.DOWN.value[0] * TILE_SIZE, DoorsCoords.DOWN.value[1] * TILE_SIZE,
                                 loadImage(self.level_type.value, -1), DoorsCoords.DOWN.value[2],
                                 DoorsCoords.DOWN.name))

    def draw(self):
        self.current_room.draw()

    def changeRoom(self, player):
        direction = player.checkDoors()

        if direction:
            dx, dy = 0, 0
            px, py = player.rect.x, player.rect.y
            match direction:
                case DoorsCoords.UP.name:
                    dy = -1
                    px = 608
                    py = 640
                case DoorsCoords.DOWN.name:
                    dy = 1
                    px = 608
                    py = 128
                case DoorsCoords.LEFT.name:
                    dx = -1
                    px = 1156
                    py = 352
                case DoorsCoords.RIGHT.name:
                    dx = 1
                    px = 128
                    py = 352
            self.current_room_coords[0] += dx
            self.current_room_coords[1] += dy
            self.current_room = self.rooms[self.current_room_coords[0]][self.current_room_coords[1]]
            self.current_room.player.collideObjects = self.current_room.objects

            player.rect.centerx, player.rect.centery = px, py

