from collections import defaultdict, OrderedDict


class Node(object):
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self._neighs = set()
        self._ncost = defaultdict(lambda:1) # stores the cost to neighbours. Default value is 1.
        self._meta = {} # space to save Node related info.

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

    def __init__(self, name=None, isDirected=False):
        self.name = name
        self.isDirected = isDirected
        self._nodes = OrderedDict()
        self._edges = []
        self._meta = {}
        self._default_unitary_cost = True


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
        

    def addEdge(self, u, v, cost=None):
        self._edges.append((u,v))
        u._neighs.add(v)
        if not self.isDirected:
            v._neighs.add(u)
        if cost is not None:
            self._default_unitary_cost = False
            u._ncost[v] = cost
            if not self.isDirected:
                v._ncost[u] = cost

    def vertexes(self):
        return self._nodes


    def edges(self):
        return self._edges
    
    def cost(self,u,v):
        '''Returns the cost from going from vertex u to v.'''
        if type(u) != Node:
            u = self._nodes[u]
        if type(v) != Node:
            v = self._nodes[v]
        if v in u._neighs:
            if self._default_unitary_cost:
                return 1
            else:
                return u._ncost[v]
        return None


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
        if self.name is not None:
            return '{}({})'.format(self.name, self._nodes.keys())
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
        

def graphToDOTFile(graph,filepath,printCost=False):
    def printEdge(edge, f, graph, printCost=False):
        if printCost:
            label = '[label="{}"]'.format(graph.cost(*edge))
        else:
            label = ''
        if graph.isDirected:
            print('{} -> {} {};'.format(*edge,label),file=f)
        else:
            print('{} -- {} {};'.format(*edge,label),file=f)

    def printVertex(v,f):
        if 'DOTFile_attributes' in v._meta:
            # https://en.wikipedia.org/wiki/DOT_(graph_description_language)#Attributes
            attr = ['{}={}'.format(k,v) for k,v in v._meta['DOTFile_attributes']]
            print('{} [label={},{}];'.format(v.name,v.name,','.join(attr)), file=f)
        elif v.data is not None:
            label = '{}({})'.format(v.name,v.data)
            print('{} [label="{}"];'.format(v.name,label),file=f)


    with open(filepath, 'w') as f:
        graphtype = 'graph' if not graph.isDirected else 'digraph'
        print('// DOT file created by script.',file=f)

        print("{} {} {{".format(graphtype, graph.name),file=f)
        if 'DOTFile_style' in graph._meta:
            print('// Custom DOT config.',file=f)
            pass # TODO: add set graph attributes/style based on _meta data.
        else:
            print('// Default DOT config.',file=f)
            print('node[shape =record];',file=f)

        print('// Describing the vertexes.',file=f)
        for v in graph.vertexes().values():
            printVertex(v,f)

        print('// Describing the edges.',file=f)
        for e in graph.edges():
            printEdge(e,f,graph, printCost=True)
            
        print('}',file=f)
        print('// End of Script',file=f)


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


def graph2mat(G, edgemap=None):
    mat = []
    order = {}
    index = [0]*len(G)
    G._meta['node2index'] = order
    G._meta['index2node'] = index
    i = 0
    for node in G.vertexes().values():
        mat.append([None for i in range(len(G))])
        order[node] = i
        index[i] = node
        mat[i][i] = 0
        i+=1
    
    if edgemap is None:
        edgemap = G.cost

    isDirected = G.isDirected
    for edge in G.edges():
        c = edgemap(*edge)
        i = order[edge[0]]
        j = order[edge[1]]
        mat[i][j] = c
        if not isDirected:
            mat[j][i] = c

    return mat




    
