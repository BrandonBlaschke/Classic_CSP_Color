from Node import Node
from typing import List
from Color import Color 

class CSP:
    """
    Performs the constriant search problem on the list of nodes given.
    """
    def __init__(self, nodes: List[Node]): 
        """
        :param nodes: List of node objects that represents a graph.
        """
        self.nodes = nodes

    def performSearch(self, node: Node):
        for color in Color:
            if node._color == None:
                node._color = color
                if self.constriant(node):
                    for neighbor in node.neighbors:
                        self.performSearch(neighbor)
                else:
                    node._color = None
            else:
                return True
        return False

    def constriant(self, node: Node):
        """
        Checks if the node is upholding the constriant for the CSP. Node can't have same color as neighbors
        :returns True if constriant is not violated, False otherwise.
        """
        for neighbor in node.neighbors:
            if neighbor._color != None and neighbor._color == node._color and node != neighbor:
                return False
        return True