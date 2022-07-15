class Mouse:
    """A mouse service interface."""

    def get_coordinates(self):
        """Gets the current mouse coordinates as a Point.
        
        Returns:
            Point: an instance of the tanks.cast.point class.
        """
        raise NotImplementedError("not implemented in base class")

    def has_mouse_moved(self):
        """Whether or not the mouse has moved since the last frame.
        
        Returns:
            bool: True if the mouse moved; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_button_down(self, button):
        """Detects if the given button is pressed.
        
        Args:
            button: a string containing the button value, e.g. 'left', 'right' or 'middle'.
            
        Returns:
            bool: True if the button is pressed; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_button_pressed(self, button):
        """Detects if the given button was pressed once.
        
        Args:
            button: a string containing the button value, e.g. 'left', 'right' or middle'
            
        Returns:
            bool: True if the button was pressed once; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_button_released(self, button):
        """Detects if the given button was released once.
        
        Args:
            button: a string containing the button value, e.g. 'left', 'right' or 'middle'
            
        Returns:
            bool: True if the button was released once; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_button_up(self, button):
        """Detects if the given button is released.
        
        Args:
            button: a string containing the button value, e.g. 'left', 'right' or 'middle'
            
        Returns:
            bool: True if button is released; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")