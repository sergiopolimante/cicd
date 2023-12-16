from grade_fast.states.node import Node
from grade_fast.states.returned import Returned


class Graded(Node):
    """
    State representing an assignment that has been graded.
    """

    @staticmethod
    def next_state() -> "Node":
        raise NotImplementedError()
