from grade_fast.states.node import Node
from grade_fast.states.returned import Returned


class Graded(Node):
    """
    State representing an assignment that has been graded.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Returns the next state in the assignment workflow.

        Returns:
        Node: The next state Returned, which is an instance of the Node class.
        """
        return Returned
