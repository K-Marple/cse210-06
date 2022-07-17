from constants import *
from game.script.action import Action


class DrawDialogAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        dialogs = cast.get_actors(DIALOG_GROUP)
        for dialog in dialogs:
            text = dialog.get_text()
            position = dialog.get_position()
            self._video.draw_text(text, position)