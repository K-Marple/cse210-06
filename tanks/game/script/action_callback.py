class ActionCallback:
    """A callback that can be used to trigger scene changes."""

    def on_next(self, scene):
        """Called when need to transition from one scene to the next.
        
        Args:
            scene: a number representing the next scene.
        """
        raise NotImplementedError("execute not implemented in base class")