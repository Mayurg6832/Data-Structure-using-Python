class Vertex:
    def __init__(self,key):
        self.id=key
        self.connected_to={}
    
    def add_neighbour(self,nbr,weight=0):
        self.connected_to[nbr]=weight
    
    def get_connections(self):
        return self.connected_to.keys()

    def get_weight(self,nbr):
        return self.connected_to[nbr]


    def __str__(self):
        return str(self.id)+'connected to'+str([x.id for x in self.connected_to])

class Graph:
    def __init__(self):
        self.number=0
        self.vertex_list={}
    
    def add_vertex(self,key):
        new_vertex=Vertex(key)
        self.vertex_list[key]=new_vertex
        self.number+=1
        return new_vertex

    def get_vertex(self,key):
        if key in self.vertex_list:
            return self.vertex_list[key]
        else:
            return None
    
    def add_edge(self,frm,to,cost=0):
        if frm not in self.vertex_list:
            self.add_vertex(frm)
        if to not in self.vertex_list:
            self.add_vertex(to)
        
        self.vertex_list[frm].add_neighbour(self.vertex_list[to])
    
    def get_vetexes_list(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())


    def __contains__(self,n):
        return n in self.vertex_list

g=Graph()
for i in range(6):
    g.add_vertex(i)


g.add_edge(0,1,2)
for vertex in g:
    print(vertex)
    print(vertex.get_connections())
