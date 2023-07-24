import random

import pygame

from src.config import TILE_SIZE
from src.level.level_config import FloorsTypes, room_base_layout
from src.objects.floor import Floor
from src.objects.wall import Wall

def loadImage(floorType, num):
    path = f"assets/sprites/room/{floorType}/"
    match num:
        case 0:
            path += f"floor{random.randint(0, 4)}.png"
        case 1:
            path += "topwall.png"
        case 2:
            path += "leftwall.png"
        case 3:
            path += "left_top_corner.png"
        case 4:
            path += "right_top_corner.png"
        case 5:
            path += "right_bottom_corner.png"
        case 6:
            path += "left_bottom_corner.png"
        case 7:
            path += "rightwall.png"
        case 8:
            path += "bottomwall.png"
    return path


class Room:
    def __init__(self, display):
        self.objects = []
        self.fillRoom()
        self.display = display

    def fillRoom(self):
        for y, row in enumerate(room_base_layout):
            for x, tile in enumerate(row):
                if [1, 2, 3, 4, 5, 6, 7, 8].__contains__(tile):
                    self.objects.append(Wall(x*TILE_SIZE, y*TILE_SIZE, loadImage(FloorsTypes.BASEMENT.value, tile)))
                elif tile == 0:
                    self.objects.append(Floor(x*TILE_SIZE, y*TILE_SIZE, loadImage(FloorsTypes.BASEMENT.value, tile)))

    def draw(self):
        for i in self.objects:
            i.update(self.display)


