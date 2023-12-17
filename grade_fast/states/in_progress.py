from grade_fast.states.graded import Graded
from grade_fast.states.node import Node


class InProgress(Node):
    """
    State representing an assignment that is currently being graded.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Returns the next state in the assignment workflow.

        Returns:
        Node: The next state Graded, which is an instance of the Node class.
        """
                
        return Graded
