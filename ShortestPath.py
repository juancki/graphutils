# Shortest path tree generated.



from collections import defaultdict
from .run import DEBUG
from .Node import graph2mat
import heapq


WHITE = 0
GRAY = 1
BLACK = 2

def DijstraSearch(G, root, satFunc):
    '''Returns the first Node in a Breath First Search that 
    satisfies the condition satFunc(Graph,Vertex) == True.
    
    Returns None otherwise'''
    if DEBUG >= 2: print('BFSearch from {}'.format(root))
    for V in Dijstra(G,root):
        if satFunc(G,V):
            return V


def Dijstra(Graph, root):
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
            color[V] = BLACK
            cost = V[0]
            vertex = V[1]
            if DEBUG >= 3: print('BFTraverse vertex {}'.format(vertex))
            yield vertex
            for neigh in G.Adj(vertex):
                if color[neigh] == WHITE:
                    parent[neigh] = vertex
                    edgecost = G.cost(vertex,neigh)
                    heapq.heappush(queue,(cost+edgecost,neigh))
            
                
def DagShortestPath(G,root):
    from .TopSort import TopologicalSort
    result = TopologicalSort(G)


def AllPairsShortestPaths(G):
    ''' '''
    W = graph2mat(G)
    L2m = W
    n = len(G)
    m = 1
    while m-1 < n:
        Lm = L2m
        L2m  = ExtendShortestPaths(Lm,Lm)
        m = 2*m
    return Lm

def ExtendShortestPaths(L,W):
    n = len(L)
    Lp = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): # this loops looks if its worth passing through k
                Lp[i][j] = ESPmin(Lp[i][j],L[i][k],W[k][j])
    return Lp

def ESPmin(lp,l,w):
    if lp is None:
        if l is not None and w is not None:
            return l+w
        return None
   
    if l is not None and w is not None:
        return min(lp,l+w)
    return lp






