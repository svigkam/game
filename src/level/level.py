import time

import pygame.image

from src.config import TILE_SIZE, SOUND_DOOR
from src.level.level_config import FloorsTypes, DoorsCoords, RoomObjects
from src.level.room import Room, loadImage
from src.objects.door import Door
from src.objects.roomObject import RoomObject


class Level:
    def __init__(self, rooms: [Room], current_room: [], level_type):
        self.rooms = rooms
        self.current_room_coords = current_room
        self.current_room: Room = rooms[current_room[0]][current_room[1]]
        self.level_type = level_type

        self.checkDoors()
        self.current_room.update_info_about_room()

    def checkDoors(self):
        for x in range(len(self.rooms)):
            for y in range(len(self.rooms[x])):
                if isinstance(self.rooms[x][y], Room):
                    if x - 1 > -1 and isinstance(self.rooms[x - 1][y], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.LEFT.value[0] * TILE_SIZE, DoorsCoords.LEFT.value[1] * TILE_SIZE,
                                 RoomObjects.DOOR.value, DoorsCoords.LEFT.value[2],
                                 DoorsCoords.LEFT.name, self.rooms[x - 1][y].is_last_room))
                    if x + 1 < len(self.rooms) and isinstance(self.rooms[x + 1][y], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.RIGHT.value[0] * TILE_SIZE, DoorsCoords.RIGHT.value[1] * TILE_SIZE,
                                 RoomObjects.DOOR.value, DoorsCoords.RIGHT.value[2],
                                 DoorsCoords.RIGHT.name, self.rooms[x + 1][y].is_last_room))
                    if y - 1 > -1 and isinstance(self.rooms[x][y - 1], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.UP.value[0] * TILE_SIZE, DoorsCoords.UP.value[1] * TILE_SIZE,
                                 RoomObjects.DOOR.value, DoorsCoords.UP.value[2], DoorsCoords.UP.name,
                                 self.rooms[x][y - 1].is_last_room))
                    if y + 1 < len(self.rooms[x]) and isinstance(self.rooms[x][y + 1], Room):
                        self.rooms[x][y].objects.append(
                            Door(DoorsCoords.DOWN.value[0] * TILE_SIZE, DoorsCoords.DOWN.value[1] * TILE_SIZE,
                                 RoomObjects.DOOR.value, DoorsCoords.DOWN.value[2],
                                 DoorsCoords.DOWN.name, self.rooms[x][y + 1].is_last_room))

    def draw(self):
        self.current_room.draw()

    def changeRoom(self, player):
        direction = player.checkDoors()

        if direction and not self.current_room.enemies:
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

            pygame.mixer.Sound(SOUND_DOOR).play()

            player.rect.centerx, player.rect.centery = px, py

