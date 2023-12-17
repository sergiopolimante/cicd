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
    Test the Assignment class to ensure it calculates the total time correctly.

    Args:
        transitions (List[Tuple[Type[Node], int]]): A list of tuples representing transitions
            between states. Each tuple contains a Node class (e.g., Submitted) and an
            associated time duration for that transition.
        expected_total_time (int): The expected total time calculated by the Assignment class.

    Raises:
        AssertionError: Raises an AssertionError if the calculated total time does not match
            the expected_total_time.
    
    Returns:
        None

    Example:
        ```python
        test_assignment_graph_transitions(
            transitions=[(Submitted, 5), (InProgress, 3), (Graded, 2)],
            expected_total_time=10
        )
        ```
    """
    assert Assignment(transitions) == expected_total_time


## I could not understand what this test is supposed to test.    
# @pytest.mark.parametrize("transitions, expected_time_between", [
#     ([(Submitted, 5), (InProgress, 3), (Graded, 2)], -2),
#     ([(Submitted, 4), (InProgress, 4)], 0),
#     ([(Submitted, 3)], -1),
#     ([], -1)  # No transitions
# ])

# def test_assignment_graph_transition_between(transitions, expected_time_between):
#     """
#     Test the AssignmentGraph to ensure it calculates the total time between two states correctly.
#     """
#     raise NotImplementedError()
