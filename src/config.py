SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
TILE_SIZE = 64
XTILES = 20
YTILES = 12

DEBUG = False

TICK_RATE = 60

DISPLAY_CAPTION = "Labirint"

# ENTITY
PLAYER_BASE_HP = 6
PLAYER_BASE_POWER = 3
PLAYER_BASE_SPEED = 3
PLAYER_SCALE = 2
PLAYER_ATTACK_DISTANCE = 85

PLAYER_FULL_HEART_IMAGE = "assets/sprites/ui/full_heart.png"
PLAYER_HALF_HEART_IMAGE = "assets/sprites/ui/half_heart.png"
PLAYER_EMPTY_HEART_IMAGE = "assets/sprites/ui/empty_heart.png"
PLAYER_COINS_IMAGE = "assets/sprites/ui/coins.png"

PLAYER_WALK_ANIMATION = [f"assets/sprites/player/walk/q ({x}).png" for x in range(1, 9)]  # 8 кадров
PLAYER_IDLE_ANIMATION = [f"assets/sprites/player/idle/q ({x}).png" for x in range(1, 6)]  # 4 кадра
PLAYER_ATTACK_ANIMATION = [f"assets/sprites/player/attack/q ({x}).png" for x in range(1, 11)]  # 11 кадра

WEAK_ENEMY_BASE_HP = 6
WEAK_ENEMY_BASE_SPEED = 1
WEAK_ENEMY_BASE_POWER = 1

NORMAL_ENEMY_BASE_HP = 1
NORMAL_ENEMY_BASE_SPEED = 1
NORMAL_ENEMY_BASE_POWER = 1

STRONG_ENEMY_BASE_SPEED = 3
STRONG_ENEMY_BASE_POWER = 3
