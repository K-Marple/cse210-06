from constants import *
from game.cast.sound import Sound
from game.script.action import Action


class CollideWallsAction(Action):

    def __init__(self, physics, audio):
        self._physics = physics
        self._audio = audio

    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        barricades = cast.get_actors(BARRICADE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        over_sound = Sound(OVER_SOUND)

        for barricade in barricades:
            tank_body = tank.get_body()
            barricade_body = barricade.get_body()

            if self._physics.has_collided(tank_body, barricade_body):
                hits = barricade.get_hits()
                stats.add_hits(hits)
                points = barricade.get_points()
                stats.add_points(points)
                cast.clear_actors(BARRICADE_GROUP)
                cast.clear_actors(BULLET_GROUP)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()

                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                else:
                    callback.on_next(GAME_OVER)
                    self._audio.play_sound(over_sound)