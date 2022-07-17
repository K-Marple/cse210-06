from constants import *
from game.script.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard):
        self._keyboard = keyboard

    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        if self._keyboard.is_key_down(LEFT):
            tank.swing_left()
        elif self._keyboard.is_key_down(RIGHT):
            tank.swing_right()
        else:
            tank.stop_moving()