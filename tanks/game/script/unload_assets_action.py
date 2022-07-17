from game.script.action import Action


class UnloadAssetsAction(Action):

    def __init__(self, audio, video):
        self._audio = audio
        self._video = video

    def execute(self, cast, script, callback):
        self._audio.unload_sounds()
        self._video.unload_fonts()
        self._video.unload_images()