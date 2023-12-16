from grade_fast.states.node import Node


class Initial(Node):
    """
    Initial state of the AssignmentGraph, not intended for normal state transition flow.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Raises an exception indicating an invalid call.

        Raises:
            Exception: Indicating that the call is invalid.

        Returns:
            Node: None
        """
        raise Exception("Invalid call to next_state on InitialState.")
