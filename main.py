# # from Node import Node
# from Color import Color
# from CSP import CSP
from GUI import GUI

# E.g On how to create custom graph

# Nodes 
# node1 = Node(None, 50, 50)
# node2 = Node(None, 500, 100)
# node3 = Node(None, 200, 500)
# nodes = [node1, node2, node3]
nodes = []

# Create Neighbors 
# node1.addNeighbor(node2)
# node1.addNeighbor(node3)

# node2.addNeighbor(node1)
# node2.addNeighbor(node3)

# node3.addNeighbor(node1)
# node3.addNeighbor(node2)

if __name__ == "__main__":
    # csp = CSP(nodes)
    # csp.performSearch(node1)
    # for node in nodes:
    #     print(node._color)
    gui = GUI(nodes)
    gui.start()