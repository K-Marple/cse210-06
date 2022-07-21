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
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "cse210-06/tanks/assets/fonts/MilitaryKid.ttf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
TANK_SOUND = "cse210-06/tanks/assets/sounds/tank_movement.wav"
FIRE_SOUND = "cse210-06/tanks/assets/sounds/tank_fire.wav"
WELCOME_SOUND = "cse210-06/tanks/assets/sounds/engaging.wav"
OVER_SOUND = "cse210-06/tanks/assets/sounds/game_over.wav"

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
UP = "up"
DOWN = "down"
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
# LEVEL_FILE = "tanks/assets/data/level-{:03}.txt"
# BASE_LEVELS = 5


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
# LEVEL_GROUP = "level"
HIT_GROUP = "hit"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
# LEVEL_FORMAT = "LEVEL: {}"
HIT_FORMAT = "HITS: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullet"
BULLET_IMAGE = "cse210-06/tanks/assets/images/000.png"
BULLET_WIDTH = 4
BULLET_HEIGHT = 6
BULLET_VELOCITY = 6

# TANK
TANK_GROUP = "tanks"
TANK_IMAGES = "cse210-06/tanks/assets/images/050.png"
TANK_WIDTH = 28
TANK_HEIGHT = 40
TANK_RATE = 6
TANK_VELOCITY = 4

# BARRICADES
BARRICADE_GROUP = "barricades"
BARRICADE_VELOCITY = 3
ROCK_BARRICADE_IMAGE = "cse210-06/tanks/assets/images\\010.png"
ROCK_BARRICADE_WIDTH = 44
ROCK_BARRICADE_HEIGHT = 44
GRASS_BARRICADE_IMAGE = "cse210-06/tanks/assets/images\\020.png"
GRASS_BARRICADE_WIDTH = 28
GRASS_BARRICADE_HEIGHT = 28
SAND_BARRICADE_IMAGE = "cse210-06/tanks/assets/images\\030.png"
SAND_BARRICADE_WIDTH = 16
SAND_BARRICADE_HEIGHT = 16
DIRT_BARRICADE_IMAGE = "cse210-06/tanks/assets/images\\040.png" 
DIRT_BARRICADE_WIDTH = 35
DIRT_BARRICADE_HEIGHT = 35
BARRICADE_POINTS_ROCK = 20
BARRICADE_POINTS_SAND = 5
BARRICADE_POINTS_GRASS = 10
BARRICADE_POINTS_DIRT = 15
BARRICADE_HIT = 1
# BARRICADE_DELAY = 0.5
# BARRICADE_RATE = 4

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
SHOOTING = "SPACE TO SHOOT"
WAS_GOOD_GAME = "GAME OVER"