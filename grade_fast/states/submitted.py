from grade_fast.states.in_progress import InProgress
from grade_fast.states.node import Node


class Submitted(Node):
    """
    State representing an assignment that has been submitted.
    """

    @staticmethod
    def next_state() -> "Node":
        raise NotImplementedError()
