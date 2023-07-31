from enum import Enum


class RoomObjects(Enum):
    LOCK = "assets/sprites/room/lock.png"
    DOOR = "assets/sprites/room/door.png"
    KEY = [f"assets/sprites/room/key/key ({x}).png" for x in range(1, 25)]
    COIN = [f"assets/sprites/room/coin/q ({x}).png" for x in range(1, 6)]
    STONE = [f"assets/sprites/room/stones/q ({x}).png" for x in range(1, 7)]
    HEALTH = [f"assets/sprites/room/health/q ({x}).png" for x in range(1, 13)]
    SPIKE = "assets/sprites/room/spike.png"
    PORTAL = [f"assets/sprites/room/portal/portal ({x}).png" for x in range(1, 5)]
    E_KEY = "assets/sprites/room/e_key.png"


class LevelsRooms(Enum):
    base_path = "assets/maps/"

    L1R1 = f"{base_path}level 1/room 1.csv"
    L1R2 = f"{base_path}level 1/room 2.csv"
    L1R3 = f"{base_path}level 1/room 3.csv"
    L1R4 = f"{base_path}level 1/room 4.csv"
    L1R5 = f"{base_path}level 1/room 5.csv"

    L2R1 = f"{base_path}level 2/room 1.csv"
    L2R2 = f"{base_path}level 2/room 2.csv"
    L2R3 = f"{base_path}level 2/room 3.csv"
    L2R4 = f"{base_path}level 2/room 4.csv"
    L2R5 = f"{base_path}level 2/room 5.csv"

    L3R1 = f"{base_path}level 3/room 1.csv"
    L3R2 = f"{base_path}level 3/room 2.csv"
    L3R3 = f"{base_path}level 3/room 3.csv"
    L3R4 = f"{base_path}level 3/room 4.csv"
    L3R5 = f"{base_path}level 3/room 5.csv"

    L4R1 = f"{base_path}level 4/room 1.csv"
    L4R2 = f"{base_path}level 4/room 2.csv"
    L4R3 = f"{base_path}level 4/room 3.csv"
    L4R4 = f"{base_path}level 4/room 4.csv"

    L5R1 = f"{base_path}level 5/room 1.csv"
    L5R2 = f"{base_path}level 5/room 2.csv"
    L5R3 = f"{base_path}level 5/room 3.csv"
    L5R4 = f"{base_path}level 5/room 4.csv"
    L5R5 = f"{base_path}level 5/room 5.csv"


class FloorsTypes(Enum):
    NECROPOLIS: str = "necropolis"
    DEPTHS: str = "depths"
    UTERO: str = "utero"
    WOMB: str = "womb"


class HelpPath(Enum):
    A = "assets/sprites/ui/A-Key.png"
    W = "assets/sprites/ui/W-Key.png"
    S = "assets/sprites/ui/S-Key.png"
    D = "assets/sprites/ui/D-Key.png"
    E = "assets/sprites/ui/E-Key.png"
    SPACE = "assets/sprites/ui/Space-Key.png"
    MOVE = [f"assets/sprites/ui/player/walk ({x}).png" for x in range(1, 9)]
    ATTACK = [f"assets/sprites/ui/player/attack ({x}).png" for x in range(1, 11)]
    ACTION = [f"assets/sprites/ui/player/door ({x}).png" for x in range(1, 11)]


class DoorsCoords(Enum):
    UP = [9, 0, 0]
    DOWN = [9, 11, 180]
    RIGHT = [19, 5, 270]
    LEFT = [0, 5, 90]
