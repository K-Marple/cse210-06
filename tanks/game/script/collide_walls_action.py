from constants import *
from game.cast.sound import Sound
from game.script.action import Action


class CollideWallsAction(Action):

    def __init__(self, physics, audio):
        self._physics = physics
        self._audio = audio

    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        walls = cast.get_actors(WALL_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for wall in walls:
            bullet_body = bullet.get_body()
            wall_body = wall.get_body()

            if self._physics.has_collided(bullet_body, wall_body):
                bullet.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio.play_sound(sound)
                points = wall.get_points()
                stats.add_points(points)
                cast.remove_actor(WALL_GROUP, wall)