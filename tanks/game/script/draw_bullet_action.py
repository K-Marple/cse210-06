from constants import *
from game.script.action import Action


class DrawBulletAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
            if bullet == None:
                return

            else:
                body = bullet.get_body()

                if bullet.is_debug():
                    rectangle = body.get_rectangle()
                    self._video.draw_rectangle(rectangle, PURPLE)

                image = bullet.get_image()
                position = body.get_position()

                y = position.get_y()
                if y <= FIELD_TOP:
                    cast.remove_actor(BULLET_GROUP, bullet)

                self._video.draw_image(image, position)