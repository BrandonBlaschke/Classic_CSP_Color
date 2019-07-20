import Color

class Node:
    """
    Represents a Node object within the graph.
    """
    def __init__(self, color: Color, posX: int, posY: int):
        """
        :param color: Color Enum 
        :param posX: X position
        :param posY: Y position
        """
        self._posX = posX
        self._posY = posY
        self._color = color
        self.neighbors = []
    
    def addNeighbor(self, neighbor):
        """
        Add a neighbor to the Node.
        :param neighbor: Node object that is to be added as a neighbor 
        """
        self.neighbors.append(neighbor)
        neighbor.neighbors.append(self)

    def setColor(self, color: Color):
        """
        Set color of Node.
        :param color: Set color of Node
        """
        self._color = color

    def getVector(self):
        """
        Vector position of the Node
        :returns Vector of Node's position x and y.
        """
        return self._posX, self._posY
