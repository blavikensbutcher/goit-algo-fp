import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас вузла дерева
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.color = "skyblue"  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # унікальний ідентифікатор

# Функція для додавання вузлів і ребер до графа
def add_edges(graph, node, pos, x=0, y=0, level=1):
    if node is not None:
        graph.add_node(node.id, label=node.val, color=node.color) # Використання id та збереження значення вузла

        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (x - 1 / (2 ** level), y - 1)
            add_edges(graph, node.left, pos, x - 1 / (2 ** level), y - 1, level + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (x + 1 / (2 ** level), y - 1)
            add_edges(graph, node.right, pos, x + 1 / (2 ** level), y - 1, level + 1)

    return graph

# Малюємо дерево
def draw_tree(root):
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(G, root, pos)

    colors = [data['color'] for _, data in G.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in G.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.show()

# Створюємо дерево з масиву (як купу)
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

# Приклад: мін-купа
heap = [1, 3, 5, 7, 9, 11, 13]

root = build_heap_tree(heap)
draw_tree(root)