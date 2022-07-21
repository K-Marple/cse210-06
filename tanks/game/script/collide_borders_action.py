from constants import *
from game.cast.sound import Sound
from game.script.action import Action
from game.cast.bullet import Bullet


class CollideBordersAction(Action):

    def __init__(self, physics, audio):
        self._physics = physics
        self._audio = audio

    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

        # fire_sound = Sound(FIRE_SOUND)
        # over_sound = Sound(OVER_SOUND)

        # if x < FIELD_LEFT:
        #     bullet.bounce_x()
        #     self._audio.play_sound(fire_sound)

        # elif x >= (FIELD_RIGHT - BULLET_WIDTH):
        #     bullet.bounce_x()
        #     self._audio.play_sound(fire_sound)

        # if y < FIELD_TOP:
        #     bullet.bounce_y()
        #     self._audio.play_sound(fire_sound)

        # elif y >= (FIELD_BOTTOM - BULLET_WIDTH):
        #     stats = cast.get_first_actor(STATS_GROUP)
        #     stats.lose_life()

        #     if stats.get_lives() > 0:
        #         callback.on_next(TRY_AGAIN)
        #     else:
        #         callback.on_next(GAME_OVER)
        #         self._audio.play_sound(over_sound)