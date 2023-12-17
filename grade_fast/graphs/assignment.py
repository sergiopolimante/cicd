


from grade_fast.states.graded import Graded
from grade_fast.states.in_progress import InProgress
from grade_fast.states.initial import Initial
from grade_fast.states.invalid import Invalid
from grade_fast.states.node import Node
from grade_fast.states.returned import Returned
from grade_fast.states.submitted import Submitted

from grade_fast.edges.edge import Edge


class Assignment():
    def __init__(self):

        self.nodes = [Initial]
        self.current_state = Initial
        
        self.edges = [Edge(Initial, 0)]
        
        self.total_time = 0

    def calculate_total_time(self) -> int:
        """
        Calculates the total time for the assignment graph.

        Returns:
            int: The total time, which is the sum of weights of all edges.

        """
        total_time = 0

        for edge in self.edges:
            total_time += edge.weight

        self.total_time = total_time
        return total_time
    
    
        




from grade_fast.states.graded import Graded
from grade_fast.states.in_progress import InProgress
from grade_fast.states.initial import Initial
from grade_fast.states.invalid import Invalid
from grade_fast.states.node import Node
from grade_fast.states.returned import Returned
from grade_fast.states.submitted import Submitted

from grade_fast.edges.edge import Edge


class Assignment():
    def __init__(self, vertices: list[tuple["Node", int]]):
        """
        Initializes an assignment graph with given vertices.

        Args:
            vertices (List[Tuple[Type[Node], int]]): A list of tuples representing vertices.
                Each tuple contains a node class (Node) (e.g., Submitted) and an associated time duration (int).

        Example:
            ```python
            assignment_instance = Assignment([(Submitted, 5), (InProgress, 3), (Graded, 2)])
            ```
        """

        self.nodes = [Initial]
        self.edges = [Edge(Initial, 0)]
        
        for vertice in vertices:
            self.nodes.append(vertice[0])
            self.edges.append(Edge(vertice[0], vertice[1]))


    def calculate_total_time(self) -> int:
        """
        Calculates the total time for the assignment graph.

        Returns:
            int: The total time, which is the sum of weights of all edges.

        """
        total_time = 0

        for edge in self.edges:
            total_time += edge.weight

        
        return total_time
        

    # I tried implementing with transition but couldn't understand the requirements from the README 
    # def transition(self, time):
    #     """
    #     Transition the current state to the next state.

    #     Args:
    #         time (int): The time taken for the transition.

    #     Returns:
    #         None
    #     """
    #     new_state = self.current_state.next_state()
    #     self.current_state = new_state
    #     self.edges.append(Edge(new_state, time))




