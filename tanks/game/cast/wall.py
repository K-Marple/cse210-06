from game.cast.actor import Actor


class Wall(Actor):
    """A solid, square object dividing things."""

    def __init__(self, body, animation, points, debug=False):
        """Constructs a new Wall.
        
        Args:
            body: a new instance of Body.
            image: a new instance of Image.
            debug: if it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points

    def get_animation(self):
        """Gets the wall's image.
        
        Returns:
            an instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the wall's body.
        
        Returns:
            an instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the wall's points.
        
        Returns:
            a number representing the wall's points.
        """
        return self._points