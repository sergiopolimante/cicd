import pytest

from grade_fast.edges.edge import Edge
from grade_fast.states import (Graded, Initial, InProgress, Invalid, Node,
                               Returned, Submitted)


@pytest.mark.parametrize("current_state, expected_state", [
    (Submitted, InProgress),
    (InProgress, Graded),
    (Graded, Returned),
    (Returned, Exception),
    (Invalid, Exception),
    (Initial, Exception),
    (Node, Exception)
])
def test_edge_transitions(current_state:Node, expected_state:Node) -> None:
    """
    Test the Edge.transition method to ensure it returns the correct next state and time taken.

    Args:
        current_state (Node): The current state of the assignment.
        expected_state (Node): The expected next state of the assignment.
    Returns:
        None
    """
    if issubclass(expected_state, Node):
        next_state = Edge.transition(current_state)
        assert next_state == expected_state
    elif issubclass(expected_state, Exception):
        with pytest.raises(expected_state):
            current_state.next_state()
