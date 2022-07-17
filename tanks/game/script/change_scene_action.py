from constants import *
from game.script.action import Action


class ChangeSceneAction(Action):
    
    def __init__(self, keyboard, next_scene):
        self._keyboard = keyboard
        self._next_scene = next_scene

    def execute(self, cast, script, callback):
        if self._keyboard.is_key_pressed(ENTER):
            callback.on_next(self._next_scene)