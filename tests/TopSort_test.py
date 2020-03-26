from ..TopSort import TopologicalSort

from ..Node import Graph
from ..DFS import *




G = Graph(isDirected=True)
G.addVertex('A')
G.addVertex('B')
G.addVertex('C')

vertexes = G.vertexes()

A = vertexes['A']
A.value = 'A'
B = vertexes['B']
B.value = 'B'
C = vertexes['C']
C.value = 'C'

G.addEdge(A,B)
G.addEdge(B,C)


assert TopologicalSort(G) == [C,B,A]


G.addVertex('D')
D = vertexes['D']
D.value = 'D'

G.addEdge(B,D)
G.addEdge(D,A)
G.addEdge(C,B)


