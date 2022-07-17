from constants import *
from game.script.action import Action
from game.cast.sound import Sound


class PlaySoundAction(Action):

    def __init__(self, audio, filename):
        self._audio = audio
        self._filename = filename

    def execute(self, cast, script, callback):
        sound = Sound(self._filename)
        self._audio.play_sound(sound)
        script.remove_action(OUTPUT, self)