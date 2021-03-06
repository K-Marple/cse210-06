from constants import *
from game.script.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        walls = cast.get_actors(BARRICADE_GROUP)
        if len(walls) == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)