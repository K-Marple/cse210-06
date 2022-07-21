from pathlib import Path
from game.script.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.load_sounds("tanks/assets/sounds")
        self._video.load_fonts("tanks/assets/fonts")
        self._video.load_images("tanks/assets/images")