


class Node(object):
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self._neighs = []

    def __str__(self):
        #   if self.data is None:
        #       return '({}:)'.format(self.name)
        #   return '({}:{})'.format(self.name,self.data)
        return self.name

    def __repr__(self):
        return str(self)


    def __lt__(self,other):
        # Heapq uses the less than (lt) comparator.
        return len(self) < len(other)


    def __len__(self):
        return len(self._neighs)



class Graph(object):

    def __init__(self, isDirected=False):
        self.isDirected = isDirected
        self._nodes = {}
        self._edges = []
        self._meta = {}


    def __len__(self):
        return len(self._nodes)

    
    def addVertex(self, vertex):
        '''Add a previously created graphutils.Node or descriptor.
        E.g:
            G = Graph()
            G.addVertex(node)
            or 
            G.addVertex('descriptor')'''
        if type(vertex) != Node:
            vertex = Node(vertex)

        self._nodes[vertex.name] = vertex
        

    def addEdge(self, u, v):
        self._edges.append((u,v))
        u._neighs.append(v)
        if not self.isDirected:
            v._neighs.append(u)

    def vertexes(self):
        return self._nodes


    def edges(self):
        return self._edges

    @staticmethod
    def getDegrees(graph):
        if not graph.isDirected:
            return {V:len(V._neighs) for V in graph.vertexes()}

        from collections import defaultdict
        indeg = defaultdict(int)
        
        for V in graph.vertexes():
            for n in V._neighs:
                indeg[n] += 1
        return {V:len(V._neighs,indeg[V]) for V in graph.vertexes()}
    
    def Adj(self,vertex):
        if type(vertex) != Node:
            vertex = self._nodes[vertex]

        return vertex._neighs

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'G({})'.format(self._nodes.keys())

def graphToFile(graph,filepath):
    with open(filepath,'w') as f:
        print('isDirected {}\n'.format(graph.isDirected), file = f )
        for v in graph.vertexes().values():
            print(v.name,end='',file=f)
            print(',',end='',file=f)
        print('', file=f)
        for e in graph.edges():
            print('{}-{}'.format(e[0],e[1]),file=f)
        

    

def graphFromFile(filepath):
    def skipBlankLines(lines):
        while lines[0] == '' or lines[0] == '\n':
            lines.pop(0)

    with open(filepath,'r') as f:
        G = Graph()
        reader = f.readlines()

        skipBlankLines(reader)
        line = reader.pop(0)
        line = line.strip('\n')

        if 'isDirected' in line:
            G.isDirected = line.split(' ')[1] == 'True'

        skipBlankLines(reader)
        vertexesLine = reader.pop(0)
        vertexesLine = vertexesLine.strip('\n')
       
        if ',' in vertexesLine:
            for vertex in vertexesLine.split(','):
                if vertex == '':
                    continue
                G.addVertex(vertex)
        
            while len(reader) != 0:
                skipBlankLines(reader)
                edgeLine = reader.pop(0)
                edgeLine = edgeLine.strip('\n')
                u,v = edgeLine.split('-')[0:2]
                u = G.vertexes()[u]
                v = G.vertexes()[v]
                G.addEdge(u,v)
            return G

        raise ValueError('File is not formatted accordingly\nisDirected True|False\nvertexes in CSV\none line per edge')



def transpose(G):
    Gt = Graph()
    Gt.isDirected = G.isDirected
    for v in G.vertexes().values():
        n = Node(v.name)
        n.data = 'T'
        Gt.addVertex(n)

    VsT  = Gt.vertexes() # Vertexes of the transpose
    for vname in G.vertexes().keys():
        vt = VsT[vname]
        for u in G.Adj(vname):
            ut = VsT[u.name]
            Gt.addEdge(ut,vt)
    return Gt






    
