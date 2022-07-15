class Physics:
    """A physics service interface."""

    def has_collided(self, subject, agent):
        """Whether or not the given subject has collided with the given agent.
        
        Args:
            subject: an instance of Body.
            agent: an instance of Body.
            
        Returns:
            bool: True if the subject had collided with the agent; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_above(self, subject, agent):
        """Whether or not the given subject is above the given agent.
        
        Args:
            subject: an instance of Body.
            agent: an instance of Body.
            
        Returns:
            bool: True if the subject is above the agent; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_below(self, subject, agent):
        """Whether or not the given subject is below the given agent.
        
        Args:
            subject: an instance of Body.
            agent: an instance of Body.
            
        Returns:
            bool: True if the subject is below the agent; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_left_of(self, subject, agent):
        """Whether or not the given subject is to the left of the given agent.
        
        Args:
            subject: an instance of Body.
            agent: an instance of Body.
            
        Returns:
            bool: True if the subject is to the left of the agent; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def is_right_of(self, subject, agent):
        """Whether or not the given subject is to the right of the given agent.
        
        Args:
            subject: an instance of Body.
            agent: an instance of Body.
            
        Returns:
            bool: True if subject is to the right of the agent; False if otherwise.
        """
        raise NotImplementedError("not implemented in base class")