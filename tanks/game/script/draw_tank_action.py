from constants import *
from game.script.action import Action


class DrawTankAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        body = tank.get_body()

        if tank.is_debug():
            rectangle = body.get_rectangle()
            self._video.draw_rectangle(rectangle, PURPLE)

        animation = tank.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video.draw_image(image, position)