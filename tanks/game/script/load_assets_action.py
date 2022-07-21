from pathlib import Path
from game.script.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.load_sounds("cse210-06/tanks/assets/sounds")
        self._video.load_fonts("cse210-06/tanks/assets/fonts")
        self._video.load_images("cse210-06/tanks/assets/images")