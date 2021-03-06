

from collections import defaultdict
from .run import DEBUG
import heapq


WHITE = 0
GRAY = 1
BLACK = 2

def BFSearch(G, satFunc, root=None):
    '''Returns the first Node in a Breath First Search that 
    satisfies the condition satFunc(Graph,Vertex) == True.
    
    Returns None otherwise'''
    if DEBUG >= 2: print('BFSearch from {}'.format(root))
    for V in BFTraverse(G,root):
        if satFunc(G,V):
            return V


def BFTraverse(G,root=None):
    time = 0
    color = defaultdict(int)
    initTime = defaultdict(int)
    parent = dict()
    G._meta['parentBFStree'] = parent
    stack = []
    if root is None:
        for vertex in G.vertexes().values():
            stack.append(vertex)
    else:
        if type(root) == str:
            # This will raise a value error if the 
            # element passed is a string but it correponds
            # to no vertex in the graph G.
            root = G.vertexes()[root]
        stack.append(root)

    while len(stack) != 0:
        while color[stack[-1]] != WHITE:
            stack.pop(-1)

        root = stack.pop(-1)
        queue = []
        queue.append((0,root))
        while len(queue) != 0:
            V = heapq.heappop(queue)
            time += 1
            initTime[V] = time
            color[V] = GRAY
            cost = V[0]
            vertex = V[1]
            if DEBUG >= 3: print('BFTraverse vertex {}'.format(vertex))
            yield vertex
            for neigh in G.Adj(vertex):
                if color[neigh] == WHITE:
                    parent[neigh] = vertex
                    heapq.heappush(queue,(cost+1,neigh))
            
                


