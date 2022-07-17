from game.script.action import Action


class ReleaseDevicesAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.release()
        self._video.release()