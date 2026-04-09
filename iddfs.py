# Tree structure (Adjacency List)
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Depth-Limited Search (helper function)
def dls(node, depth, limit, visited):
    if depth > limit:
        return

    visited.append(node)

    for neighbor in tree[node]:
        dls(neighbor, depth + 1, limit, visited)


# Iterative Deepening DFS
def iddfs(root, max_depth):
    for limit in range(max_depth + 1):
        visited = []
        dls(root, 0, limit, visited)
        print(f"Depth Limit {limit}: Visited nodes {visited}")


# Main
root = 1
max_depth = 2

iddfs(root, max_depth)