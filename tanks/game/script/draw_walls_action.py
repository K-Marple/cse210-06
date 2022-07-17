from constants import *
from game.script.action import Action


class DrawWallsAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        walls = cast.get_actors(WALL_GROUP)

        for wall in walls:
            body = wall.get_body()

            if wall.is_debug():
                rectangle = body.get_rectangle()
                self._video.draw_rectangle(rectangle, PURPLE)

            animation = wall.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video.draw_image(image, position)