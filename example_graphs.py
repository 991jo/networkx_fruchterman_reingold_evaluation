import networkx as nx
import numpy as np

cube = nx.cubical_graph()
grid_2d = nx.grid_2d_graph(5, 5)
random_graph = nx.gnp_random_graph(15, 0.2, seed=42)
tree = nx.balanced_tree(3, 3)
snake = nx.Graph()
snake.add_edges_from(zip(range(0, 20), range(1, 21)))

ball = nx.complete_graph(30)
ball_and_chain = nx.complete_graph(30)
ball_and_chain.add_edges_from(zip(range(0, -5, -1), range(-1, -6, -1)))

small_ball_and_chain = nx.complete_graph(5)
small_ball_and_chain.add_edges_from(zip(range(0, -5, -1), range(-1, -6, -1)))

eades_6b = nx.Graph()
eades_6b.add_edges_from(
    [
        (1, 2),
        (2, 3),
        (3, 1),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 5),
        (5, 8),
        (8, 9),
        (9, 10),
        (10, 8),
        (9, 11),
        (8, 12),
        (12, 4),
        (12, 13),
        (13, 14),
        (14, 15),
        (15, 16),
        (16, 17),
        (17, 13),
    ]
)

example_1 = nx.Graph()
example_1.add_edges_from(
    [
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 8),
        (5, 8),
        (8, 9),
        (8, 10),
    ]
)

all_graphs = [
    (cube, "Cube", None),
    (grid_2d, "2D Grid", 1000),
    (random_graph, "Random Graph", None),
    (tree, "Tree", 200),
    (snake, "Snake", 1000),
    (ball, "Ball", None),
    (ball_and_chain, "Ball and Chain", None),
    (small_ball_and_chain, "Small Ball and Chain", None),
    (eades_6b, "Eades 6b", None),
    (example_1, "example graph 1", None),
]


def draw(graph, iterations):
    pos = nx.drawing.spring_layout(graph, iterations=100)
    nx.draw(graph, pos=pos)


def diameters(pos):
    pos = np.fromiter(pos.values(), np.dtype((float, 2)))

    # difference between point i and j (vector from j to i)
    delta = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]

    # distance between points
    return np.linalg.norm(delta, axis=-1)
