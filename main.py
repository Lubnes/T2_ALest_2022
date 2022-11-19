from graph import Vertex

class Vertex:
    #connections = []
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add(self, name):
        self.connections.append(name)

class Graph:
    def __init__(self, dict):
        self.dict = dict 


myGraph = {}

with open('caso1.txt', 'r') as file:
    
    f = file.readlines()

for line in f:
    words = line.replace('\n', '').split(' -> ')
    key = words[0]
    value = words[1]
    if key not in myGraph:
        #valueList = [value]
        #print(value)
        myGraph[key] = []

    myGraph[key].append(value)

    if value not in myGraph:
        myGraph.setdefault(value, [])
    #print(words)

print("Dicionário:\n", myGraph)

# parent = {s: None}
# def dfs(adjacencies, start):
#     for v in adjacencies[s]:
#         if v not in parent:
#             parent[v] = s
#             dfs(adjacencies, s)

# def dfs(vertice):
#     color[vertice]="cinza"
#     dfs_output.append(vertice)
#     for sabor in myGraph[vertice]:#sabor adjacente ao vertice 
#         if color[sabor] == "branco":
#             parent[sabor]=vertice
#             dfs(sabor)
#     color[vertice] = "preto"

# dfs("flocos")

combinacoes = []

keys = myGraph.keys()
values = myGraph.values()

#visited = []
visited = set(())

#combs = []
combs = set(())
#combs_three = []      # [...,i,j,k,...]
#combs_two = []

def dfs(myGraph):
    for k in keys:
        if k not in visited:
            dfs_visit(k, myGraph)
    print("Combinações de sorvetes: ", combs)
    
def dfs_visit(vertex, graph):
    sorvetes = [] #continuar
    #if vertex not in visited:
        #visited.add(vertex)
    for v in myGraph[vertex]:
        print(v)
        if v not in visited:
            sorvetes.append(v)
            dfs_visit(v, visited)
            #calcula(sorvetes)

def firstOnes(myGraph, keys):
    k = set(())
    v = set(())
    first = []
    for i in keys:
        v.add(myGraph[keys])
        k = first.union(i)
        first = k.difference(v)
    return first
        
        

def calcula(sorvetes):
    i = 0
    j = i+1
    k = j+1
    for i in sorvetes:
        for j in sorvetes:
            myTuple2 = tuple((i, j))
            combs.add(myTuple2)
            for k in sorvetes:
                myTuple3 = tuple((i, j, k))
                combs.add(myTuple3)

#dfs('frutas_cristalizadas', myGraph)

for i in myGraph:
    print("key - value:")
    print("key: ", i, " --> ", "value: ", myGraph[i])
    # print("Tipo myGraph[i]: ", type(myGraph[i]))
    # print("Tipo myGraph.get(i): ", type(myGraph.get(i)))

# for i in myGraph:
#     print("key - value:")
#     print("key: ", i, " --> ", "value: ", myGraph.get(i))