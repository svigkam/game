SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
TILE_SIZE = 64
XTILES = 20
YTILES = 12

DEBUG = False

TICK_RATE = 60

DISPLAY_CAPTION = "Labirint"

# SOUNDS

SOUND_PLAYER_WALK = "assets/sounds/move.wav"
SOUND_PLAYER_ATTACK = "assets/sounds/pattack.wav"
SOUND_PLAYER_DAMAGE = "assets/sounds/pdamage.wav"
SOUND_PLAYER_DEATH = "assets/sounds/pdeath.wav"

SOUND_COIN_UP = "assets/sounds/collect.wav"
SOUND_HEALTH_UP = "assets/sounds/health.wav"
SOUND_DOOR = "assets/sounds/door.wav"
SOUND_PURCHASE = "assets/sounds/kassa.wav"
SOUND_SELECT = "assets/sounds/select.wav"
SOUND_TELEPORT = "assets/sounds/teleport.wav"


SOUND_ZOMBIE_WALK = "assets/sounds/move.wav"
SOUND_ZOMBIE_ATTACK = "assets/sounds/zattack.wav"
SOUND_ZOMBIE_DAMAGE = "assets/sounds/zdamage.wav"
SOUND_ZOMBIE_DEATH = "assets/sounds/zdeath.wav"

SOUND_MINOTAUR_WALK = "assets/sounds/move.wav"
SOUND_MINOTAUR_ATTACK = "assets/sounds/mattack.wav"
SOUND_MINOTAUR_DAMAGE = "assets/sounds/mdamage.wav"
SOUND_MINOTAUR_DEATH = "assets/sounds/mdeath.wav"

SOUND_SNAKE_WALK = "assets/sounds/move.wav"
SOUND_SNAKE_ATTACK = "assets/sounds/sattack.wav"
SOUND_SNAKE_DAMAGE = "assets/sounds/sdamage.wav"
SOUND_SNAKE_DEATH = "assets/sounds/sdeath.wav"

SOUND_WIZARD_WALK = "assets/sounds/move.wav"
SOUND_WIZARD_ATTACK = "assets/sounds/wattack.wav"
SOUND_WIZARD_DAMAGE = "assets/sounds/wdamage.wav"
SOUND_WIZARD_DEATH = "assets/sounds/wdeath.wav"


# PLAYER
PLAYER_HP = 6
PLAYER_POWER = 6
PLAYER_SPEED = 6
PLAYER_SCALE = 2
PLAYER_ATTACK_DISTANCE = 140

PLAYER_FULL_HEART_IMAGE = "assets/sprites/ui/full_heart.png"
PLAYER_HALF_HEART_IMAGE = "assets/sprites/ui/half_heart.png"
PLAYER_EMPTY_HEART_IMAGE = "assets/sprites/ui/empty_heart.png"
PLAYER_COINS_IMAGE = "assets/sprites/ui/coins.png"
SWORD_IMAGE = "assets/sprites/ui/shield.png"

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

MINOTAUR_HP = 8
MINOTAUR_SPEED = 2
MINOTAUR_POWER = 1
MINOTAUR_SCALE = 1.5
MINOTAUR_ATTACK_DISTANCE = 35

MINOTAUR_WALK_ANIMATION = [f"assets/sprites/minotaur/walk/walk ({x}).png" for x in range(1, 8)]
MINOTAUR_IDLE_ANIMATION = [f"assets/sprites/minotaur/idle/idle ({x}).png" for x in range(1, 6)]
MINOTAUR_ATTACK_ANIMATION = [f"assets/sprites/minotaur/attack/attack ({x}).png" for x in range(1, 7)]
MINOTAUR_INJURY_ANIMATION = [f"assets/sprites/minotaur/injury/injury ({x}).png" for x in range(1, 4)]
MINOTAUR_DEATH_ANIMATION = [f"assets/sprites/minotaur/death/death ({x}).png" for x in range(1, 7)]

# SNAKE

SNAKE_HP = 8
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

WIZARD_HP = 10
WIZARD_SPEED = 1
WIZARD_POWER = 1
WIZARD_SCALE = 1.5
WIZARD_ATTACK_DISTANCE = 50

WIZARD_WALK_ANIMATION = [f"assets/sprites/wizard/walk/walk ({x}).png" for x in range(1, 13)]
WIZARD_IDLE_ANIMATION = [f"assets/sprites/wizard/idle/idle ({x}).png" for x in range(1, 6)]
WIZARD_ATTACK_ANIMATION = [f"assets/sprites/wizard/attack/attack ({x}).png" for x in range(1, 13)]
WIZARD_INJURY_ANIMATION = [f"assets/sprites/wizard/injury/injury ({x}).png" for x in range(1, 4)]
WIZARD_DEATH_ANIMATION = [f"assets/sprites/wizard/death/death ({x}).png" for x in range(1, 10)]

# BOSS

BOSS_HP = 80
BOSS_SPEED = 2
BOSS_POWER = 1
BOSS_SCALE = 3
BOSS_ATTACK_DISTANCE = 50

BOSS_WALK_ANIMATION = [f"assets/sprites/boss/idle/idle ({x}).png" for x in range(1, 5)]
BOSS_IDLE_ANIMATION = [f"assets/sprites/boss/idle/idle ({x}).png" for x in range(1, 5)]
BOSS_ATTACK_ANIMATION = [f"assets/sprites/boss/attack/attack ({x}).png" for x in range(1, 7)]
BOSS_INJURY_ANIMATION = [f"assets/sprites/boss/injury/injury ({x}).png" for x in range(1, 5)]
BOSS_DEATH_ANIMATION = [f"assets/sprites/boss/death/death ({x}).png" for x in range(1, 19)]
BOSS_SKILL_ANIMATION = [f"assets/sprites/boss/skill/skill ({x}).png" for x in range(1, 13)]

