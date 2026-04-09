from collections import deque

# Tree structure
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def bfs(tree, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for neighbor in tree[node]:
            queue.append(neighbor)

    return visited


# Main
root = 1
result = bfs(tree, root)

print("BFS Traversal:", *result)