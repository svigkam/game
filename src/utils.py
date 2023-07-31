from src.config import TILE_SIZE
from src.level.level import Level
from src.level.level_config import LevelsRooms, FloorsTypes, HelpPath
from src.level.room import Room

import csv

from src.objects.coin import Coin
from src.objects.help_object import HelpObject


def csv_to_map(path) -> []:
    with open(path.value) as file:
        result = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')]
    return result


def add_help_signs(room):
    room.append(HelpObject(5 * TILE_SIZE, 2 * TILE_SIZE, path=HelpPath.W.value))
    room.append(HelpObject(4 * TILE_SIZE, 3 * TILE_SIZE, path=HelpPath.A.value))
    room.append(HelpObject(5 * TILE_SIZE, 4 * TILE_SIZE, path=HelpPath.S.value))
    room.append(HelpObject(5 * TILE_SIZE, 3 * TILE_SIZE, anim=HelpPath.MOVE.value))
    room.append(HelpObject(6 * TILE_SIZE, 3 * TILE_SIZE, path=HelpPath.D.value))

    room.append(HelpObject(11 * TILE_SIZE, 3 * TILE_SIZE, anim=HelpPath.ACTION.value))
    room.append(HelpObject(11 * TILE_SIZE, 2 * TILE_SIZE, path=HelpPath.E.value))

    room.append(HelpObject(15 * TILE_SIZE, 3 * TILE_SIZE, anim=HelpPath.ATTACK.value))
    room.append(HelpObject(15 * TILE_SIZE, 2 * TILE_SIZE, path=HelpPath.SPACE.value))


def initLevels(disp, player):
    l1type = FloorsTypes.NECROPOLIS
    l2type = FloorsTypes.DEPTHS
    l3type = FloorsTypes.DEPTHS
    l4type = FloorsTypes.WOMB
    l5type = FloorsTypes.UTERO

    level1 = Level([
        [Room(disp, csv_to_map(LevelsRooms.L1R3), l1type, player),
         Room(disp, csv_to_map(LevelsRooms.L1R4), l1type, player),
         Room(disp, csv_to_map(LevelsRooms.L1R5), l1type, player, True)],
        [Room(disp, csv_to_map(LevelsRooms.L1R1), l1type, player), 0, 0],
        [Room(disp, csv_to_map(LevelsRooms.L1R2), l1type, player), 0, 0],
    ], [1, 0], l1type)

    add_help_signs(level1.rooms[1][0].objects)

    level2 = Level([
        [Room(disp, csv_to_map(LevelsRooms.L2R4), l2type, player),
         Room(disp, csv_to_map(LevelsRooms.L2R3), l2type, player),
         Room(disp, csv_to_map(LevelsRooms.L2R2), l2type, player)],
        [Room(disp, csv_to_map(LevelsRooms.L2R5), l2type, player, True), 0,
         Room(disp, csv_to_map(LevelsRooms.L2R1), l2type, player)],
        [0, 0, 0],
    ], [1, 2], l2type)

    level3 = Level([
        [Room(disp, csv_to_map(LevelsRooms.L3R3), l3type, player), 0, 0],
        [Room(disp, csv_to_map(LevelsRooms.L3R2), l3type, player),
         Room(disp, csv_to_map(LevelsRooms.L3R4), l3type, player), 0],
        [Room(disp, csv_to_map(LevelsRooms.L3R1), l3type, player),
         Room(disp, csv_to_map(LevelsRooms.L3R5), l3type, player, True), 0],
    ], [2, 0], l3type)

    level4 = Level([
        [Room(disp, csv_to_map(LevelsRooms.L4R2), l4type, player),
         Room(disp, csv_to_map(LevelsRooms.L4R3), l4type, player),
         Room(disp, csv_to_map(LevelsRooms.L4R4), l4type, player, True)],
        [Room(disp, csv_to_map(LevelsRooms.L4R1), l4type, player), 0, 0],
        [0, 0, 0],
    ], [1, 0], l4type)

    level5 = Level([
        [0, 0, Room(disp, csv_to_map(LevelsRooms.L5R2), l5type, player)],
        [0, 0, Room(disp, csv_to_map(LevelsRooms.L5R1), l5type, player)],
        [Room(disp, csv_to_map(LevelsRooms.L5R5), l5type, player, True),
         Room(disp, csv_to_map(LevelsRooms.L5R4), l5type, player),
         Room(disp, csv_to_map(LevelsRooms.L5R3), l5type, player)],
    ], [1, 2], l5type)

    return [level1, level2, level3, level4, level5]
