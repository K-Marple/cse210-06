from constants import *
from game.script.action import Action


class DrawBulletAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()

        if bullet.is_debug():
            rectangle = body.get_rectangle()
            self._video.draw_rectangle(rectangle, PURPLE)

        image = bullet.get_image()
        position = body.get_position()
        self._video.draw_image(image, position)