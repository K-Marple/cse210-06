from constants import *
from game.script.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        bullets = cast.get_first_actor(BULLET_GROUP)
        for bullet in bullets:
            if bullet == None:
                return

            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)