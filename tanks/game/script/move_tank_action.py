from constants import *
from game.cast.point import Point
from game.script.action import Action


class MoveTankAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        body = tank.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - TANK_WIDTH):
            position = Point(SCREEN_WIDTH - TANK_WIDTH, position.get_y())
        
        elif y < 0:
            position = Point(position.get_x(), 0)
        elif y > (SCREEN_HEIGHT - TANK_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - TANK_HEIGHT)

        body.set_position(position)