from grade_fast.states.graded import Graded
from grade_fast.states.node import Node


class InProgress(Node):
    """
    State representing an assignment that is currently being graded.
    """

    @staticmethod
    def next_state() -> "Node":
        raise NotImplementedError()
