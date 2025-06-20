import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.color = "#bbbbbb"
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, level=1):
    if node is not None:
        graph.add_node(node.id, label=node.val, color=node.color)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / (2 ** level), y - 1)
            add_edges(graph, node.left, pos, x - 1 / (2 ** level), y - 1, level + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / (2 ** level), y - 1)
            add_edges(graph, node.right, pos, x + 1 / (2 ** level), y - 1, level + 1)

    return graph


def draw_tree(root):
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(G, root, pos)

    colors = [data['color'] for _, data in G.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in G.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.show()


def build_heap_tree(array):
    nodes = [Node(val) for val in array]

    for i in range(len(nodes)):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(nodes):
            nodes[i].left = nodes[left_i]
        if right_i < len(nodes):
            nodes[i].right = nodes[right_i]

    return nodes[0] if nodes else None


def generate_colors(n):
    colors = []
    for i in range(n):
        brightness = int(50 + 205 * (i + 1) / n)  # від #3232f0 до #ffffff
        color = f'#{brightness:02x}{brightness:02x}f0'
        colors.append(color)
    return colors


def dfs_iterative(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # правий — перший у стеку (бо лівий має бути зверху)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def bfs_iterative(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited


def visualize_traversal(root, order='dfs'):
    if order == 'dfs':
        nodes = dfs_iterative(root)
    elif order == 'bfs':
        nodes = bfs_iterative(root)
    else:
        raise ValueError("Unsupported order. Use 'dfs' or 'bfs'.")

    colors = generate_colors(len(nodes))

    for i, node in enumerate(nodes):
        node.color = colors[i]

    draw_tree(root)
    



heap = [1, 3, 5, 7, 9, 11, 13]
root = build_heap_tree(heap)

# DFS візуалізація
# visualize_traversal(root, order='dfs')

# BFS візуалізація
visualize_traversal(root, order='bfs')