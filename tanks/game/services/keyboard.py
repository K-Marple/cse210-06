class Keyboard:
    """A keyboard service interface."""

    def is_key_down(self, key):
        """Detects if the given key is being pressed.
        
        Args:
            key: a string containing the key value, e.g. 'a', '0', etc.
            
        Returns:
            bool: True if the key is being pressed; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_key_pressed(self, key):
        """Detects if the given key was pressed once.
        
        Args:
            key: a string containing the key value, e.g. 'a', '0', etc.
            
        Returns:
            bool: True if the key was pressed once; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_key_released(self, key):
        """Detects if the given key was released once.
        
        Args:
            key: a strings containing the key value, e.g. 'a', '0', etc.
            
        Returns:
            bool: True if the key was released once; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_key_up(self, key):
        """Detects if the given key is released.
        
        Args:
            key: a string containing  the key value, e.g. 'a', '0', etc.
            
        Returns:
            bool: True if the key is released; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")