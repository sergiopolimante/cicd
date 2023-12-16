from abc import ABC, abstractmethod


class Node(ABC):
    """
    Abstract base class representing a state of an assignment.
    """

    @staticmethod
    @abstractmethod
    def next_state() -> "Node":
        raise NotImplementedError()
