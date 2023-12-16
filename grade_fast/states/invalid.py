from grade_fast.states.node import Node


class Invalid(Node):
    """
    State representing an invalid state transition.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Invalid call as there is no valid next state from InvalidState. Raises an exception.

        Raises:
            Exception: Indicating that the call is invalid.

        Returns:
            Node: None
        """
        raise Exception("Invalid state transition.")
