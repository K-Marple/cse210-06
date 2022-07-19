class Image:
    """An image."""

    def __init__(self, filename, scale=1, rotation=0):
        """Constructs a new Image."""
        self._filename = filename
        self._scale = scale
        self._rotation = rotation

    def get_filename(self):
        """Gets the name of the image file.
        
        Returns:
            a string containing the name of the image file.
        """
        return self._filename

    def get_rotation(self):
        """Gets teh degrees the image should be rotation.
        
        Returns:
            a float representing the degrees the image should be rotated.
        """
        return self._rotation

    def get_scale(self):
        """Gets the scaling factor for the image.
        
        Returns:
            a float representing the scaling factor for the image.
        """
        return self._scale

    def set_rotation(self, rotation):
        """Sets the image's rotation to the given value.
        
        Args:
            rotation: a float representing the degree of rotation (clockwise).
        """
        self._rotation = rotation

    def set_scale(self, scale):
        """Sets the image's scale to the given value.
        
        Args:
            scale: a float representing how much the image should be scaled.
        """
        self._scale = scale