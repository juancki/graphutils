


from ..Node import Node, Graph, graphFromFile, graphToFile, graphToDOTFile



# Create temporary file with graph
text='''isDirected True
A,B,C
A-B
B-C
A-C
'''

FILEPATH_FROM = '/tmp/testingGraphFromFile'
FILEPATH_TO = '/tmp/testingGraphToFile'

# test Graph formation an graphFromFile
with open(FILEPATH_FROM, 'w') as f:
    f.write(text)
    f.flush()
    f.close()
    
    G = graphFromFile(FILEPATH_FROM)
    vertexes = G.vertexes()

    assert len(vertexes) == 3

    edges = G.edges()

    assert len(edges) == 3

    A = vertexes['A'] 
    B = vertexes['B'] 
    C = vertexes['C'] 
    A.data = 32

    assert B in A._neighs
    assert not A in B._neighs
    assert C in B._neighs
    assert not B in C._neighs
    assert not A in C._neighs

    G.addEdge(C,B)

    assert B in C._neighs

    G.addVertex('E')
    E = vertexes['E']
    G.addEdge(A,E)

    assert E in A._neighs
    assert not A in E._neighs

    G.addEdge(E,A)

    assert A in E._neighs

    graphToFile(G,FILEPATH_TO)
    graphToDOTFile(G,FILEPATH_TO+'.dot')
    Q = graphFromFile(FILEPATH_TO)




import os
os.remove(FILEPATH_FROM)
os.remove(FILEPATH_TO)
os.remove(FILEPATH_TO+'.dot')


