#!/usr/local/bin/python3

import sys
from mjcgraph.digraph import digraph
from mjcgraph import draw

DG = digraph.Digraph('../data/tinyDG.txt')
print(DG.to_string())
print(DG.G)

fig = draw.Draw(digraph=True)
fig.node_attr(fontsize='8')
fig.draw(DG, [11, 12, 9, 11])
