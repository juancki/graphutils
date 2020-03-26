

from .DFS import DFTraverse
from .run import DEBUG


def TopologicalSort(G):
    result = []
    for vertex,times in DFTraverse(G):
        if times[1] is not None:
            if DEBUG >=2: print('TopologicalSort vertex {}, times {}'.format(vertex,times))
            result.append(vertex)

    return result













