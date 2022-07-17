from game.script.action import Action


class InitializeDevicesAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.initialize()
        self._video.initialize()