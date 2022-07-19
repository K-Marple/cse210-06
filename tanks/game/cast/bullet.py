import random
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

    def bounce_x(self):
        """Bounces the bullet in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the bullet in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

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
        """Release the bullet in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BULLET_VELOCITY * rn, BULLET_VELOCITY * rn])
        vy = -BULLET_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)