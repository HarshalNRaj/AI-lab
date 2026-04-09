class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # list of child nodes

    def add_child(self, child):
        self.children.append(child)


def depth_limited_search(node, limit, depth=0, visited=None):
    if visited is None:
        visited = []

    # Visit the current node
    visited.append(node.value)
    print(node.value, end=" ")

    # If depth limit reached, stop expanding
    if depth == limit:
        return

    # Recur for all children
    for child in node.children:
        depth_limited_search(child, limit, depth + 1, visited)

    return visited


# -------- Example Tree --------
# Creating nodes
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')

# Building tree
A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(G)

# -------- Run DLS --------
depth_limit = 2
print("Depth-Limited Search Traversal:")
visited_nodes = depth_limited_search(A, depth_limit)