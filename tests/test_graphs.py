import pytest

from grade_fast.graphs.assignment import Assignment
from grade_fast.states import Graded, InProgress, Submitted


@pytest.mark.parametrize("transitions, expected_total_time", [
    ([(Submitted, 5), (InProgress, 3), (Graded, 2)], 10),
    ([(Submitted, 4), (InProgress, 4)], 8),
    ([(Submitted, 3)], 3),
    ([], 0)  # No transitions
])
def test_assignment_graph_transitions(transitions, expected_total_time):
    """
    Test the AssignmentGraph to ensure it calculates the total time correctly.
    """
    raise NotImplementedError()

@pytest.mark.parametrize("transitions, expected_time_between", [
    ([(Submitted, 5), (InProgress, 3), (Graded, 2)], -2),
    ([(Submitted, 4), (InProgress, 4)], 0),
    ([(Submitted, 3)], -1),
    ([], -1)  # No transitions
])
def test_assignment_graph_transition_between(transitions, expected_time_between):
    """
    Test the AssignmentGraph to ensure it calculates the total time between two states correctly.
    """
    raise NotImplementedError()
