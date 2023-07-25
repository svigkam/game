import random

from src.config import TILE_SIZE
from src.entites.enemy import Enemy
from src.level.level_config import FloorsTypes
from src.objects.floor import Floor
from src.objects.wall import Wall

def loadImage(floorType, num):
    path = f"assets/sprites/room/{floorType}/"
    match num:
        case 0:  # Пол
            path += f"floor{random.randint(0, 4)}.png"
        case 1:  # стена сверху
            path += "topwall.png"
        case 2:  # стена слева
            path += "leftwall.png"
        case 3:  # левый верхний угол
            path += "left_top_corner.png"
        case 4:  # правый верхний угол
            path += "right_top_corner.png"
        case 5:  # правый нижний угол
            path += "right_bottom_corner.png"
        case 6:  # левый нижний угол
            path += "left_bottom_corner.png"
        case 7:  # правая стена
            path += "rightwall.png"
        case 8:  # нижняя стена
            path += "bottomwall.png"
    return path


class Room:
    def __init__(self, display, layout, player):
        self.layout = layout
        self.objects = []
        self.enemies = [Enemy(100, 200, 52, 80, player), Enemy(500, 500, 52, 80, player)]
        self.display = display

        self.fillRoom()

    def fillRoom(self):
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if [1, 2, 3, 4, 5, 6, 7, 8].__contains__(tile):
                    self.objects.append(Wall(x*TILE_SIZE, y*TILE_SIZE, loadImage(FloorsTypes.BASEMENT.value, tile)))
                elif tile == 0:
                    self.objects.append(Floor(x*TILE_SIZE, y*TILE_SIZE, loadImage(FloorsTypes.BASEMENT.value, tile)))

        for enemy in self.enemies:
            enemy.collideObjects = self.objects

    def draw(self):
        for i in self.objects:
            i.update(self.display)
        for enemy in self.enemies:
            enemy.update(self.display)
            if enemy.is_dead:
                self.enemies.remove(enemy)

    def addDoors(self):
        pass


