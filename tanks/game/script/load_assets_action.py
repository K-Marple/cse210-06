from pathlib import Path
from game.script.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.load_sounds("tank/assets/sounds")
        self._video.load_fonts("tank/assets/fonts")
        self._video.load_images("tank/assets/images")