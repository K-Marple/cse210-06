from game.cast.point import Point
from game.cast.rectangle import Rectangle


class Body:
    """A rigid body used for physics operations."""

    def __init__(self, position=Point(), size=Point(), velocity=Point()):
        """Constructs a new Body."""
        self._position = position
        self._size = size
        self._velocity = velocity

    def get_position(self):
        """Gets the body's position.
        
        Args:
            an instance of Point containing the x and y coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the body's size.
        
        Returns:
            an instance of Point containing with width and height.
        """
        return self._size

    def get_velocity(self):
        """Gets the body's velocity.
        
        Returns:
            an instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity

    def get_rectangle(self):
        """Gets the rectangle enclosing the body.
        
        Returns:
            an instance of Rectangle.
        """
        return Rectangle(self._position, self._size)

    def set_position(self, position):
        """Sets the position to the given value.
        
        Args:
            position: an instance of Point.
        """
        self._position = position

    def set_size(self, size):
        """Sets the size to the given value.
        
        Args:
            size: an instance of Point.
        """
        self._size = size

    def set_velocity(self, velocity):
        """Sets the velocity to the given value.
        
        Args:
            velocity: an instance of Point.
        """
        self._velocity = velocity