if __name__ == '__main__':
    import sys
else:
    from ..Node import Graph
    from ..DFS import *

from ..Node import Graph
from ..DFS import *




G = Graph(isDirected=True)
G.addVertex('A')
G.addVertex('B')
G.addVertex('C')
G.addVertex('D')

vertexes = G.vertexes()

A = vertexes['A']
A.value = 'A'
B = vertexes['B']
B.value = 'B'
C = vertexes['C']
C.value = 'C'
D = vertexes['D']
D.value = 'D'

G.addEdge(A,B)
G.addEdge(B,C)

assert DFSearchNode(G,A,C)

assert not DFSearchNode(G,B,A)

G.addEdge(B,D)
G.addEdge(D,A)
G.addEdge(C,B)

assert DFSearchNode(G,B,A)

