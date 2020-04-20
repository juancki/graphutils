

from .DFS import DFTraverse
from .run import DEBUG


def TopologicalTraverse(G):
    for vertex,times in DFTraverse(G):
        if times[1] is not None:
            if DEBUG >=2: print('TopologicalSort vertex {}, times {}'.format(vertex,times))
            yield vertex

def TopologicalSort(G):
    return list(TopologicalTraverse(G))
    result = []
    for vertex in TopologicalTraverse(G):
        result.append(vertex)
    return result













