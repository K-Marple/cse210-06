from game.script.action import Action


class StartDrawingAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        self._video.clear_buffer()