
from ..Node import Graph
from ..BFS import *




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

assert BFSearch(G,lambda G,V: V == C, root=A) is C

assert BFSearch(G,lambda G,V: V == A, root=B) is None


G.addEdge(B,D)
G.addEdge(D,A)
G.addEdge(C,B)

assert BFSearch(G,lambda G,V: V == A,root=B) is A

