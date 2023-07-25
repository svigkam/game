from src.level.level import Level
from src.level.level_config import room_base_layout
from src.level.room import Room


def initLevels(disp, player):
    level1 = Level([
        [Room(disp, room_base_layout, player), Room(disp, room_base_layout, player), Room(disp, room_base_layout, player)],
        [Room(disp, room_base_layout, player), 0, 0],
        [Room(disp, room_base_layout, player), 0, 0],
    ], [0, 0])
    return level1

