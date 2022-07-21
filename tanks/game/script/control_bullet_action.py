from constants import *
from game.script.action import Action
from game.cast.point import Point
from game.cast.image import Image
from game.cast.bullet import Bullet
from game.cast.body import Body
from game.cast.sound import Sound


class ControlBulletAction(Action):

    def __init__(self, keyboard, audio):
        self._keyboard = keyboard
        self._audio = audio

    def execute(self, cast, script, callback):
        if self._keyboard.is_key_pressed(SPACE):
            bullet = self._add_bullet(cast)
            sound = Sound(FIRE_SOUND)
            self._audio.play_sound(sound)
            bullet.release()

    def _add_bullet(self, cast):
        tank = cast.get_first_actor(TANK_GROUP)
        tank_position = tank.get_body().get_position()
        x = tank_position.get_x() + (TANK_WIDTH / 2) - (BULLET_WIDTH / 2)
        y = tank_position.get_y() - 2
        position = Point(x, y)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BULLET_IMAGE)
        bullet = Bullet(body, image, True)
        cast.add_actor(BULLET_GROUP, bullet)
        return bullet