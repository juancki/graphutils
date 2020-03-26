#
#
from collections import defaultdict, namedtuple
from .run import DEBUG

WHITE = 0
GRAY = 1
BLACK = 2

def DFSearchValue(G,value):
    for vertex,_ in DFTraverse(G):
        if vertex.data == value:
            return vertex


def DFSearchNode(G,start,node):
    if DEBUG >= 1: print('DFSearchNode From {} To {}'.format(start,node))
    for vertex,_ in DFTraverse(G,start):
        if DEBUG >= 2: print('DFSearchNode\t:',vertex)
        if vertex == node:
            return True
    return False


def DFTraverse(G,start = None):
    time = 0
    color = defaultdict(int)
    initTime = defaultdict(int)
    parent = dict()
    G._meta['parentDFStree'] = parent
    stack = []
    if start is None:
        for vertex in G.vertexes().values():
            stack.append(vertex)
    else:
        stack.append(start)

    while len(stack) != 0:
        V = stack.pop(-1)
        if DEBUG >= 3: print('DFTraverse analyzing:',V,'. Stack:',stack)
        if color[V] == WHITE:
            time+=1
            initTime[V] = time
            color[V] = GRAY
            yield V,(initTime[V],None)
            stack.append(V)
            for neigh in reversed(G.Adj(V)):
                if color[neigh] == WHITE:
                    parent[neigh] = V
                    stack.append(neigh)

            
        elif color[V] == GRAY:
            #set fin time
            color[V] = BLACK
            time += 1
            yield V,(initTime[V],time)





