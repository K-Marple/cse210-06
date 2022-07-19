from game.cast.actor import Actor


class Label(Actor):
    """A label to be displayed."""

    def __init__(self, text, position, debug=False):
        """Constructs a new Label.
        
        Args:
            text: an instance of Text.
            position: an instance of Point.
        """
        super().__init__(debug)
        self._text = text
        self._position = position

    def get_position(self):
        """Gets the label's position.
        
        Returns:
            an instance of Point.
        """
        return self._position

    def get_text(self):
        """Gets the label's text.
        
        Returns:
            an instance of Text.
        """
        return self._text