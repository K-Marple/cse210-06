from constants import *
from game.cast.sound import Sound
from game.script.action import Action


class CollideTankAction(Action):

    def __init__(self, physics, audio):
        self._physics = physics
        self._audio = audio

    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        tank = cast.get_first_actor(TANK_GROUP)

        bullet_body = bullet.get_body()
        tank_body = tank.get_body()

        if self._physics.has_collided(bullet_body, tank_body):
            bullet.bounce_y()
            sound = Sound(FIRE_SOUND)
            self._audio.play_sound(sound)