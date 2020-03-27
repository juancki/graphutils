# Strongly connected componentes

from .Node import transpose
from .TopSort import TopologicalSort
from collections import defaultdict
from .run import DEBUG


WHITE = 0
GRAY = 1
BLACK = 2

def SCC(G):
    ordered = TopologicalSort(G)
    Gt = transpose(G)
    G._meta['Gt'] = Gt
    if DEBUG >=2: print('SCC TopologicalSort:',ordered)
    return ComponentTraverse(Gt,ordered)

            
def ComponentTraverse(Gt,ordered):
    roots = []
    index_of = defaultdict(int)
    edges = defaultdict(set)

    Components = dict()
    Components['roots'] = roots
    Components['edges'] = edges
    Components['index_of'] = index_of
    Components['comp'] = [0]
    
    
    index = 0 # 0 is for the unassigned
    
    stack = [ u.name for u in ordered]
    while len(stack) != 0:
        possibleRoot = Gt.vertexes()[stack.pop(-1)]

        if index_of[possibleRoot] != 0:
            continue

        index += 1
        root = possibleRoot
        roots.append(root)
        if DEBUG >= 3: print('ComponentTraverse root:',root)
        Components['comp'].append(list())

        s2 = [] # Second stack
        s2.append(root)
        while len(s2) != 0:
            V = s2.pop(-1)
            if index_of[V] == 0: # if V is unassigned
                index_of[V] = index
                Components['comp'][index].append(V)
                for neighV in Gt.Adj(V):
                    if index_of[neighV] == 0:
                        s2.append(neighV)
                        
                    elif index_of[neighV] == index:
                        pass
                    else:
                        edges[index_of[neighV]].add(index)
        # yield Componentes['comp'][index]
    return Components

        




    
