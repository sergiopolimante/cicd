from grade_fast.states.graded import Graded
from grade_fast.states.node import Node

class Edge():
    
    def __init__(self, destiny_node: "Node",  weight: int):
        """
        Initializes an edge in a linear graph.

        Args:
            destiny_node (Node): The destination node connected by this edge.
            weight (int): The weight associated with this edge.

        Example:
            ```python
            edge_instance = Edge(InProcess, 5)
            ```
        """

        # we don't need an origin node since our graph is linear
        self.destiny_node = destiny_node
        self.weight = weight


    def transition(node:"Node") -> "Node":
        """
        Returns the next state given the current state node. 

        Args:
            node (Node): The current state node.

        Returns:
            Node: The next state, which is an instance of the Node class.

        Example:
            ```python
            next_state_instance = edge_instance.transition(current_state_instance)
            ```
        """
        return node.next_state()
    
    
