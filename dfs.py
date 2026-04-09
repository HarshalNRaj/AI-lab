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

def dfs(tree, node, visited):
    visited.append(node)

    for neighbor in tree[node]:
        dfs(tree, neighbor, visited)

    return visited


# Main
root = 1
result = dfs(tree, root, [])

print("DFS Traversal:", *result)