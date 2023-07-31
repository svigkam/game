SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
TILE_SIZE = 64
XTILES = 20
YTILES = 12

DEBUG = False

TICK_RATE = 60

DISPLAY_CAPTION = "Labirint"

# PLAYER
PLAYER_HP = 12
PLAYER_POWER = 12
PLAYER_SPEED = 8
PLAYER_SCALE = 2
PLAYER_ATTACK_DISTANCE = 140

PLAYER_FULL_HEART_IMAGE = "assets/sprites/ui/full_heart.png"
PLAYER_HALF_HEART_IMAGE = "assets/sprites/ui/half_heart.png"
PLAYER_EMPTY_HEART_IMAGE = "assets/sprites/ui/empty_heart.png"
PLAYER_COINS_IMAGE = "assets/sprites/ui/coins.png"

PLAYER_WALK_ANIMATION = [f"assets/sprites/player/walk/walk ({x}).png" for x in range(1, 9)]
PLAYER_IDLE_ANIMATION = [f"assets/sprites/player/idle/idle ({x}).png" for x in range(1, 6)]
PLAYER_ATTACK_ANIMATION = [f"assets/sprites/player/attack/attack ({x}).png" for x in range(1, 11)]
PLAYER_INJURY_ANIMATION = [f"assets/sprites/player/injury/injury ({x}).png" for x in range(1, 6)]
PLAYER_DEATH_ANIMATION = [f"assets/sprites/player/death/death ({x}).png" for x in range(1, 7)]

# ZOMBIE

ZOMBIE_HP = 6
ZOMBIE_SPEED = 1
ZOMBIE_POWER = 1
ZOMBIE_SCALE = 1.5
ZOMBIE_ATTACK_DISTANCE = 15

ZOMBIE_WALK_ANIMATION = [f"assets/sprites/zombie/walk/walk ({x}).png" for x in range(1, 12)]
ZOMBIE_IDLE_ANIMATION = [f"assets/sprites/zombie/idle/idle ({x}).png" for x in range(1, 11)]
ZOMBIE_ATTACK_ANIMATION = [f"assets/sprites/zombie/attack/attack ({x}).png" for x in range(1, 9)]
ZOMBIE_INJURY_ANIMATION = [f"assets/sprites/zombie/injury/injury ({x}).png" for x in range(1, 7)]
ZOMBIE_DEATH_ANIMATION = [f"assets/sprites/zombie/death/death ({x}).png" for x in range(1, 9)]

# MINOTAUR

MINOTAUR_HP = 6
MINOTAUR_SPEED = 1
MINOTAUR_POWER = 1
MINOTAUR_SCALE = 1.5
MINOTAUR_ATTACK_DISTANCE = 35

MINOTAUR_WALK_ANIMATION = [f"assets/sprites/minotaur/walk/walk ({x}).png" for x in range(1, 8)]
MINOTAUR_IDLE_ANIMATION = [f"assets/sprites/minotaur/idle/idle ({x}).png" for x in range(1, 6)]
MINOTAUR_ATTACK_ANIMATION = [f"assets/sprites/minotaur/attack/attack ({x}).png" for x in range(1, 7)]
MINOTAUR_INJURY_ANIMATION = [f"assets/sprites/minotaur/injury/injury ({x}).png" for x in range(1, 4)]
MINOTAUR_DEATH_ANIMATION = [f"assets/sprites/minotaur/death/death ({x}).png" for x in range(1, 7)]

# SNAKE

SNAKE_HP = 6
SNAKE_SPEED = 1
SNAKE_POWER = 1
SNAKE_SCALE = 1.5
SNAKE_ATTACK_DISTANCE = 50

SNAKE_WALK_ANIMATION = [f"assets/sprites/snake/walk/walk ({x}).png" for x in range(1, 16)]
SNAKE_IDLE_ANIMATION = [f"assets/sprites/snake/idle/idle ({x}).png" for x in range(1, 9)]
SNAKE_ATTACK_ANIMATION = [f"assets/sprites/snake/attack/attack ({x}).png" for x in range(1, 13)]
SNAKE_INJURY_ANIMATION = [f"assets/sprites/snake/injury/injury ({x}).png" for x in range(1, 7)]
SNAKE_DEATH_ANIMATION = [f"assets/sprites/snake/death/death ({x}).png" for x in range(1, 10)]

# WIZARD

WIZARD_HP = 6
WIZARD_SPEED = 1
WIZARD_POWER = 1
WIZARD_SCALE = 1.5
WIZARD_ATTACK_DISTANCE = 50

WIZARD_WALK_ANIMATION = [f"assets/sprites/wizard/walk/walk ({x}).png" for x in range(1, 13)]
WIZARD_IDLE_ANIMATION = [f"assets/sprites/wizard/idle/idle ({x}).png" for x in range(1, 6)]
WIZARD_ATTACK_ANIMATION = [f"assets/sprites/wizard/attack/attack ({x}).png" for x in range(1, 13)]
WIZARD_INJURY_ANIMATION = [f"assets/sprites/wizard/injury/injury ({x}).png" for x in range(1, 4)]
WIZARD_DEATH_ANIMATION = [f"assets/sprites/wizard/death/death ({x}).png" for x in range(1, 10)]

