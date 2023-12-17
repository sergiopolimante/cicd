from grade_fast.states.node import Node


class Returned(Node):
    """
    State representing an assignment that has been returned to the student.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Invalid call as there is no valid next state from Returned. Raises an exception.

        Raises:
            Exception: Indicating that the call is invalid.

        Returns:
            Node: None
        """        
        raise Exception("Invalid state transition.")
