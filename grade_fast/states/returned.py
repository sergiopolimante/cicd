from grade_fast.states.node import Node


class Returned(Node):
    """
    State representing an assignment that has been returned to the student.
    """

    @staticmethod
    def next_state() -> "Node":
        raise NotImplementedError()
