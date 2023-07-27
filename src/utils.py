import pygame

from src.level.level import Level
from src.level.level_config import LevelsRooms, FloorsTypes
from src.level.room import Room

import csv


def csv_to_map(path) -> []:
    with open(path.value) as file:
        result = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')]
    return result


def initLevels(disp, player):
    l1type = FloorsTypes.NECROPOLIS
    level1 = Level([
        [Room(disp, csv_to_map(LevelsRooms.L1R3), l1type, player), Room(disp, csv_to_map(LevelsRooms.L1R1), l1type, player), Room(disp, csv_to_map(LevelsRooms.L1R2), l1type, player)],
        [Room(disp, csv_to_map(LevelsRooms.L1R4), l1type, player), 0, 0],
        [Room(disp, csv_to_map(LevelsRooms.L1R5), l1type, player, True), 0, 0],
    ], [0, 0], l1type)

    # level2 = Level([
    #     [Room(disp, csv_to_map(LevelsRooms.L2R4), player), Room(disp, csv_to_map(LevelsRooms.L2R5), player, True), 0],
    #     [Room(disp, csv_to_map(LevelsRooms.L2R3), player), 0, 0],
    #     [Room(disp, csv_to_map(LevelsRooms.L2R2), player), Room(disp, csv_to_map(LevelsRooms.L2R1), player), 0],
    # ], [1, 2])
    #
    # level3 = Level([
    #     [Room(disp, csv_to_map(LevelsRooms.L3R3), player), Room(disp, csv_to_map(LevelsRooms.L3R2), player), Room(disp, csv_to_map(LevelsRooms.L3R1), player)],
    #     [0, Room(disp, csv_to_map(LevelsRooms.L3R4), player), Room(disp, csv_to_map(LevelsRooms.L3R5), player, True)],
    #     [0, 0, 0],
    # ], [2, 0])
    #
    # level4 = Level([
    #     [Room(disp, csv_to_map(LevelsRooms.L4R2), player), Room(disp, csv_to_map(LevelsRooms.L4R1), player), 0],
    #     [Room(disp, csv_to_map(LevelsRooms.L4R3), player), 0, 0],
    #     [Room(disp, csv_to_map(LevelsRooms.L4R4), player, True), 0, 0],
    # ], [1, 0])
    #
    # level5 = Level([
    #     [0, 0, Room(disp, csv_to_map(LevelsRooms.L5R5), player, True)],
    #     [0, 0, Room(disp, csv_to_map(LevelsRooms.L5R4), player)],
    #     [Room(disp, csv_to_map(LevelsRooms.L5R2), player), Room(disp, csv_to_map(LevelsRooms.L5R1), player), Room(disp, csv_to_map(LevelsRooms.L5R3), player)],
    # ], [1, 2])

    return level1
