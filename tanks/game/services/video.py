class Video:
    """A video service interface."""

    def clear_buffer(self):
        """Prepares the buffer for drawing."""
        raise NotImplementedError("not implemented in base class")

    def draw_image(self, image, position):
        """Draws the given image on the buffer at the given position. The image won't
        appear on the screen until the flush_buffer() is called.
        
        Args:
            image: an instance of tanks.cast.image.
            position: an instance of tanks.cast.point.
            
        Raises:
            KeyError: if the image file hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_rectangle(self, size, position, color):
        """Draws a rectangle on the buffer at the given position. The rectangle won't
        appear on the screen until flush_buffer() is called.
        
        Args:
            size: an instance of tanks.cast.point.
            position: an instance of tanks.cast.point.
            color: an instance of tanks.cast.color.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_text(self, text, position):
        """Draws the given text on the buffer at the given position. The text won't
        appear on the screen until flush_buffer() is called.
        
        Args:
            text: an instance of tanks.cast.text.
            position: an instance of tanks.cast.point.
            
        Raises:
            KeyError: if the font file for the text hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")
    
    def flush_buffer(self):
        """Swaps the buffers, displaying everything that has been drawn on the screen."""
        raise NotImplementedError("not implemented in base class")
    
    def initialize(self):
        """Initializes underlying video device. This method should be called before the
        main game loop begins."""
        raise NotImplementedError("not implemented in base class")

    def is_window_open(self):
        """Wether or not the window is open.
        
        Returns:
            bool: True if window is open; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def load_fonts(self, directory):
        """Loads all the fonts in the given directory and sub-directories.
        
        Args:
            directory: a string containing the absolute folder path where font files are stored.
        """
        raise NotImplementedError("not implemented in base class")
    
    def load_images(self, directory):
        """Loads all the images in the given directory and sub-directories.
        
        Args:
            directory: a string containing the absolute folder path where image files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def release(self):
        """Releases the underlying video device. This method should be called after the game
        loop has finished running."""
        raise NotImplementedError("not implemented in base class")
    
    def unload_fonts(self):
        """Unloads all fonts that were previously loaded."""
        raise NotImplementedError("not implemented in base class")
    
    def unload_images(self):
        """Unloads all images that were previously loaded."""
        raise NotImplementedError("not implemented in base class")