from abc import ABC, abstractmethod


class Node(ABC):
    """
    Abstract base class representing a state of an assignment.
    """

    @staticmethod
    @abstractmethod
    def next_state() -> "Node":
        """
        Returns the next state in the assignment workflow.

        Returns:
        Node: The next state, which is an instance of the Node class.

        """       
        raise Exception("Invalid state transition.")
    