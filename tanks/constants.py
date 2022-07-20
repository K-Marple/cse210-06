import pathlib

from pyray import get_gamepad_name
from game.cast.color import Color

# GENERAL GAME CONSTANTS

# GAME
GAME_NAME = "Tanks"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "tanks/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
MOVEMENT_SOUND = "tanks/assets/sounds/tank_movement.wav"
FIRE_SOUND = "tanks/assets/sounds/tank_fire.wav"
WELCOME_SOUND = "tanks/assets/sounds/start.wav"
OVER_SOUND = "tanks/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "tanks/assets/data/level-{:03}.txt"
BASE_LEVELS = 5


# SCRIPTING CONSTANTS

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6


# CASTING CONSTANTS

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullet"
BULLET_IMAGE = "tanks/assets/images/000.png"
BULLET_WIDTH = 28
BULLET_HEIGHT = 28
BULLET_VELOCITY = 6

# TANK
TANK_GROUP = "tanks"
TANK_IMAGES = "tanks/assets/images/050.png"
TANK_WIDTH = 106
TANK_HEIGHT = 28
TANK_RATE = 6
TANK_VELOCITY = 7

# WALL
WALL_GROUP = "bricks"
WALL_IMAGES = {
    "r": [f"tanks/assets/images/{i:03}.png" for i in range(10, 19)],
    "g": [f"tanks/assets/images/{i:03}.png" for i in range(20, 29)],
    "s": [f"tanks/assets/images/{i:03}.png" for i in range(30, 39)],
    "d": [f"tanks/assets/images/{i:03}.png" for i in range(40, 49)]
}
WALL_WIDTH = 80
WALL_HEIGHT = 28
WALL_DELAY = 0.5
WALL_RATE = 4
WALL_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "WARMING THE ENGINES"
WAS_GOOD_GAME = "GAME OVER"