import pygame

from src.config import TILE_SIZE
from src.entites.enemy import Enemy
from src.entites.minotaur import Minotaur
from src.entites.snake import Snake
from src.entites.wizard import Wizard
from src.entites.zombie import Zombie

from src.objects.coin import Coin
from src.objects.floor import Floor
from src.objects.key import Key
from src.objects.portal import Portal
from src.objects.wall import Wall
from src.objects.spike import Spike
from src.objects.stone import Stone
from src.objects.health import Health


def loadImage(floor_type, num):
    return f"assets/sprites/room/{floor_type}/{num}.png"


class Room:
    def __init__(self, display, layout, room_type, player, last_room=False):
        self.display = display
        self.layout = layout
        self.room_type = room_type
        self.is_last_room = last_room

        self.player = player
        self.objects = []
        self.enemies = []

        self.fillRoom()
        self.update_info_about_room()

    def fillRoom(self):
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile in range(1, 9):
                    self.objects.append(Wall(x * TILE_SIZE, y * TILE_SIZE, loadImage(self.room_type.value, tile)))
                else:
                    self.objects.append(Floor(x * TILE_SIZE, y * TILE_SIZE, loadImage(self.room_type.value, 0)))
                    if tile == 505:
                        self.enemies.append(Zombie(x * TILE_SIZE, y * TILE_SIZE, self.player))
                    elif tile == 606:
                        self.enemies.append(Minotaur(x * TILE_SIZE, y * TILE_SIZE, self.player))
                    elif tile == 707:
                        self.enemies.append(Snake(x * TILE_SIZE, y * TILE_SIZE, self.player))
                    elif tile == 808:
                        self.enemies.append(Wizard(x * TILE_SIZE, y * TILE_SIZE, self.player))
                    elif tile == 11:
                        self.objects.append(Coin(x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 12:
                        self.objects.append(Key(x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 13:
                        self.objects.append(Spike(x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 14:
                        self.objects.append(Stone(x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 15:
                        self.objects.append(Health(x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 100:
                        self.objects.append(Portal(x * TILE_SIZE, y * TILE_SIZE))

    def draw(self):

        for i in self.objects[:]:
            if i.to_clear:
                self.update_info_about_room(delete=True, i=i)
            if len(self.enemies) == 0 and i.visible == False:
                i.visible = True
            i.update(self.display)

        for enemy in self.enemies:
            enemy.update(self.display)
            if enemy.is_dead:
                self.enemies.remove(enemy)
                self.player.empty_level = True if len(self.enemies) == 0 else False

    def update_info_about_room(self, delete=False, i=None):
        if delete:  # delete
            if i in self.objects:
                self.objects.remove(i)
            for enemy in self.enemies:
                if i in enemy.collideObjects:
                    enemy.collideObjects.remove(i)
            if i in self.player.collideObjects:
                self.player.collideObjects.remove(i)
        else:  # update
            for enemy in self.enemies:
                enemy.collideObjects = self.objects
            self.player.collideObjects = self.objects
