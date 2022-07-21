from constants import *
from game.cast.actor import Actor
from game.cast.point import Point


class Barricade(Actor):
    """A solid object dividing things."""

    def __init__(self, body, image, points, hits, debug=False):
        """Constructs a new Barricade.
        
        Args:
            body: a new instance of Body.
            image: a new instance of Image.
            debug: if it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points
        self._hits = hits

    def get_body(self):
        """Gets the barricade's body.
        
        Returns:
            an instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the barricade's image.
        
        Returns:
            an instance of Image.
        """
        return self._image

    def set_image(self, next_image):
        """Changes the image to a new one.
        
        Args:
            next_image: an new instance of Image.
            
        Returns:
            an instance of Image.
        """
        self._image = next_image

        return self._image

    def fall(self):
        vx = 0
        vy = BARRICADE_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_points(self):
        """Gets the barricade's points.
        
        Returns:
            a number representing the points.
        """
        return self._points

    def get_hits(self):
        """Gets the number of barricades hit.
        
        Returns:
            a number representing that a barricade was hit.
        """
        return self._hits