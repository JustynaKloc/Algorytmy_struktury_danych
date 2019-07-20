from Queue import Queue
from subprocess import call

class Graph_Node():
    def __init__(self, name):
        self.name=name
        self.attr={}
        self.neighbours={}
    def add_neighbour(self,  other_node,  weight=0):
        self.neighbours[other_node]=weight
    def set_attribute(self, atr, val):
        self.attr[atr]=val
    def get_attribute(self, atr):
        if atr in self.attr.keys():
            return self.attr[atr]
        else:
            return None
    def get_neighbours(self):
        return self.neighbours.keys()
    def get_weight(self, other_node):
        return self.neighbours[other_node]
    def clear_attributes(self):
        self.attr={}
    def __str__(self):
        msg="Vertex "+str(self.name)+" with attributes-"
        for k, v in self.attr.items():
            if not v.__class__ == Graph_Node:
                msg+=" "+str(k)+": "+str(v)
            else:
                msg+=" "+str(k)+": "+str(v.name)
        return msg

class myGraph():
    def __init__(self):
        self.nodes={}
        self.num_nodes=0
    def addVertex(self, vert):
        self.num_nodes+=1
        new_node=Graph_Node(vert)
        self.nodes[vert]=new_node
    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.nodes.keys():
            self.addVertex(fromVert)
        if toVert not in self.nodes.keys():
            self.addVertex(toVert)
        self.nodes[fromVert].add_neighbour(self.nodes[toVert], weight)
    def getVertex(self,  vertKey):
        if vertKey in self.nodes.keys():
            return self.nodes[vertKey]
        else:
            return None
    def getVertices(self):
        return self.nodes.keys()
    def getEdges(self):
        l=[]
        for k in self.nodes.keys():
            node=self.nodes[k]
            for n in node.get_neighbours():
                l.append((k, n.name,  node.get_weight(self.nodes[n.name])))
        return l
    def DOT_dump(self, name="graph_dump"):
        print("rysowanie...", end='')
        with open(name+".dot", "w") as f:
            f.write("digraph {\n")
            for edge in self.getEdges():
                f.write('"'+str(edge[0])+'" -> "'+str(edge[1])+'"\n')
            f.write("}")
        call(["dot", "-Tpng", name+".dot", "-o", name+".png"])
        print("gotowe.")
    def BFS(self, start): #przeszukiwanie wszerz 
        start=self.getVertex(start)
        if start:
            for node in self:
                node.set_attribute("colour", "white")
                node.set_attribute("prev",  None)
            start.set_attribute("dist",  0)
            q=Queue()
            q.enqueue(start)
            while (q.size()>0):
                current_node = q.dequeue()
                for nbr in current_node.get_neighbours():
                    if nbr.get_attribute("colour")=='white':
                        nbr.set_attribute("colour",  "gray")
                        nbr.set_attribute("prev",  current_node)
                        nbr.set_attribute("dist",  current_node.get_attribute("dist")+1)
                        q.enqueue(nbr)
                current_node.set_attribute("colour",  "black")
        else:
            raise("No such element in graph.")
    def DFS(self, current): #przeszukiwanie w głąb
        current=self.getVertex(current)
        if current:
            for node in self:
                node.set_attribute("Visited", False)
            self.count=0
            self.ret_val=[]
            self._DFS(current)
            return self.ret_val[::-1]
        else:
            raise("No such element in graph.")
    def _DFS(self, current):
        self.count+=1
        current.set_attribute("Visited",  True)
        current.set_attribute("Start",  self.count)
        for nbr in current.get_neighbours():
            if not nbr.get_attribute("Visited"):
                self._DFS(nbr)
        self.count+=1
        current.set_attribute("Finish",  self.count)
        self.ret_val.append(current)
    def find_shortest(self, fromVert): #szukanie najkrótszej drogi 
        self.BFS(fromVert)
        ret_val={}
        buffer=[]
        for node in self:
            a=node
            while a.get_attribute("prev"):
                buffer.append(a.get_attribute("prev"))
                a=a.get_attribute("prev")
            ret_val[node]=buffer[::-1]
            buffer=[]
        return ret_val
    def clear_nodes(self):
        for node in self:
            node.clear_attributes()
    def __contains__(self,  n):
        return n in self.nodes
    def __iter__(self):
        return iter(self.nodes.values())
    def __str__(self):
        msg="Graph with:"
        for node in self:
            msg+="\n"+str(node)
        return msg

if __name__=="__main__":
    n="abcdef"
    G=myGraph()
    for letter in n:
        G.addVertex(letter)
    print(G.getVertices())
    G.addEdge('a', 'b', 1)
    G.addEdge('a', 'b')
    G.addEdge('c', 'f', 3)
    G.addEdge('d', 'f', 4)
    G.addEdge('b', 'd')
    G.addEdge('d', 'e')
    print(G.getEdges())
    G.DOT_dump()
    s=G.DFS('a')
    for node in s:
        print(node)
    print(G)
    p=G.find_shortest('a')
    for k, v in p.items():
        msg=k.name+": "
        for i,  pathelement in enumerate(v):
            msg+=pathelement.name+" -> "
        msg+=k.name
        print(msg)
