from constants import *
from game.script.action import Action


class DrawHudAction(Action):

    def __init__(self, video):
        self._video = video

    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, HIT_GROUP, HIT_FORMAT, stats.get_hits())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives())
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())

    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video.draw_text(text, position)