from constants import *
from game.script.action import Action
from game.cast.point import Point


class DrawWallsAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        barricades = cast.get_actors(BARRICADE_GROUP)

        for barricade in barricades:
            body = barricade.get_body()

            if barricade.is_debug():
                rectangle = body.get_rectangle()
                self._video.draw_rectangle(rectangle, PURPLE)

            image = barricade.get_image()
            position = body.get_position()

            x = position.get_x()
            y = position.get_y()

            if y >= (FIELD_BOTTOM):
                y = FIELD_TOP
                position = Point(x, (y - 44))
                body.set_position(position)

            self._video.draw_image(image, position)