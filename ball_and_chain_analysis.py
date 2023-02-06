from example_graphs import ball, ball_and_chain, diameters
from math import sqrt
import networkx as nx
import numpy as np

SAMPLES = 10

k_ball = sqrt(1/len(ball.nodes))
k_ball_and_chain = sqrt(1/len(ball_and_chain.nodes))

ball_diameters = []
ball_and_chain_diameters = []

for _ in range(SAMPLES):

    pos = nx.drawing.spring_layout(ball, scale=None)
    diameter = np.max(diameters(pos))
    ball_diameters.append(diameter)

    pos = nx.drawing.spring_layout(ball_and_chain, scale=None)
    ball_pos = {k: v for k, v in pos.items() if k >= 0}
    diameter = np.max(diameters(ball_pos))
    ball_and_chain_diameters.append(diameter)

print(0.2*k_ball)
print(sum(ball_diameters)/SAMPLES)
print(0.2*k_ball_and_chain)
print(sum(ball_and_chain_diameters)/SAMPLES)
