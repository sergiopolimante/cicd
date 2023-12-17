from grade_fast.states.in_progress import InProgress
from grade_fast.states.node import Node


class Submitted(Node):
    """
    State representing an assignment that has been submitted.
    """

    @staticmethod
    def next_state() -> "Node":
        """
        Returns the next state in the assignment workflow.

        Returns:
        Node: The next state InProgress, which is an instance of the Node class.

        """
        return InProgress
