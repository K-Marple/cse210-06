from constants import *
from game.script.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard):
        self._keyboard = keyboard

    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        if self._keyboard.is_key_down(LEFT):
            tank.move_left()
        elif self._keyboard.is_key_down(RIGHT):
            tank.move_right()
        elif self._keyboard.is_key_down(UP):
            tank.move_up()
        elif self._keyboard.is_key_down(DOWN):
            tank.move_down()
        else:
            tank.stop_moving()