from src.config import TILE_SIZE
from src.objects.roomObject import RoomObject


class Floor(RoomObject):
    def __init__(self, x, y, path):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, path)
