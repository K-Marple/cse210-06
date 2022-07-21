import random
from constants import *
from game.script.action import Action
from game.cast.point import Point
from game.cast.image import Image
from game.cast.wall import Barricade
from game.cast.body import Body


class ControlBarricadeAction(Action):

    def __init__(self, keyboard):
        self._keyboard = keyboard
        self._count = 0

    def execute(self, cast, script, callback):
        self._count += 1

        if (self._count % 80) == 0:
            barricade = self._add_barricade(cast)
            barricade.fall()

    def _add_barricade(self, cast):
        barricade_options = [ROCK_BARRICADE_IMAGE, DIRT_BARRICADE_IMAGE, SAND_BARRICADE_IMAGE, GRASS_BARRICADE_IMAGE]
        image_file = random.choice(barricade_options)
        if image_file == ROCK_BARRICADE_IMAGE:
            x = random.choice(0, (SCREEN_WIDTH - ROCK_BARRICADE_WIDTH))
            y = 0 - ROCK_BARRICADE_HEIGHT
            size = Point(ROCK_BARRICADE_WIDTH, ROCK_BARRICADE_HEIGHT)
            points = BARRICADE_POINTS_ROCK

        elif image_file == DIRT_BARRICADE_IMAGE:
            x = random.choice(0, (SCREEN_WIDTH - DIRT_BARRICADE_WIDTH))
            y = 0 - DIRT_BARRICADE_HEIGHT
            size = Point(DIRT_BARRICADE_WIDTH, DIRT_BARRICADE_HEIGHT)
            points = BARRICADE_POINTS_DIRT

        elif image_file == SAND_BARRICADE_IMAGE:
            x = random.choice(0, (SCREEN_WIDTH - SAND_BARRICADE_WIDTH))
            y = 0 - SAND_BARRICADE_HEIGHT
            size = Point(SAND_BARRICADE_WIDTH, SAND_BARRICADE_HEIGHT)
            points = BARRICADE_POINTS_SAND

        elif image_file == GRASS_BARRICADE_IMAGE:
            x = random.choice(0, (SCREEN_WIDTH - GRASS_BARRICADE_WIDTH))
            y = 0 - GRASS_BARRICADE_HEIGHT
            size = Point(GRASS_BARRICADE_WIDTH, GRASS_BARRICADE_HEIGHT)
            points = BARRICADE_POINTS_GRASS

        image = Image(image_file)
        position = Point(x, y)
        velocity = Point(0, BARRICADE_VELOCITY)
        body = Body(position, size, velocity)

        hits = BARRICADE_HIT

        barricade = Barricade(body, image, points, hits)
        cast.add_actor(BARRICADE_GROUP, barricade)
        return barricade