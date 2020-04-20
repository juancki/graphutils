
from ..ShortestPath import AllPairsShortestPaths
from ..Node import Node, Graph



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
G.addEdge(B,C,cost=3)
G.addEdge(C,D)
G.addEdge(D,A,cost=4)

allpairs =  AllPairsShortestPaths(G)
assert str(allpairs) == '[[0, 1, 4, 5], [8, 0, 3, 4], [5, 6, 0, 1], [4, 5, 8, 0]]'



G2 = Graph()
G2.isDirected = True


G2.addVertex('a')
G2.addVertex('b')
G2.addVertex('c')
G2.addVertex('d')
G2.addVertex('e')
G2.addVertex('f')
G2.addVertex('g')
G2.addVertex('h')

v2 = G2.vertexes()
# a: b
G2.addEdge(v2['a'],v2['b'])
# b: c,e,f
G2.addEdge(v2['b'],v2['c'])
G2.addEdge(v2['b'],v2['e'])
G2.addEdge(v2['b'],v2['f'])
# c: d,g
G2.addEdge(v2['c'],v2['d'])
G2.addEdge(v2['c'],v2['g'])
# d: c,h
G2.addEdge(v2['d'],v2['c'])
G2.addEdge(v2['d'],v2['h'])
# e: a,f
G2.addEdge(v2['e'],v2['a'])
G2.addEdge(v2['e'],v2['f'])
# f: g
G2.addEdge(v2['f'],v2['g'])
# g: f,h
G2.addEdge(v2['g'],v2['f'])
G2.addEdge(v2['g'],v2['h'])
# h: h
G2.addEdge(v2['h'],v2['h'])

allpairs2 = AllPairsShortestPaths(G2)



