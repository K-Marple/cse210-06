from constants import *
from game.cast.actor import Actor
from game.cast.point import Point


class Bullet(Actor):
    """A solid, penitrating object that flies at high velocity."""

    def __init__(self, body, image, debug=False):
        """Constructs a new Bullet.
        
        Args:
            body: a new instance of Body.
            image: a new instance of Image.
            debug: if it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            an instance of Body.
        """
        return self._body

    def get_images(self):
        """Gets the bullet's image.
        
        Returns:
            an instance of Image.
        """
        return self._image

    def release(self):
        """Release the bullet in a straight direction."""
        vx = 0
        vy = -BULLET_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)