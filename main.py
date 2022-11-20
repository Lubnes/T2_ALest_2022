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


def dfs(graph):
    #visited = []
    visited = set(())
    #combs = []
    combinations = set(())
    #combinations_three = []      # [...,i,j,k,...]
    #combinations_two = []
    combine = []
    comb_count = 0
    objective = firstOnes(graph)
    for i in objective:
        dfs_visit(i, graph, visited, combine, comb_count, combinations)
        # if k not in visited:
        #     dfs_visit(k, myGraph)
    print("Combinações de sorvetes: ", combinations)
    
def dfs_visit(vertex, graph, visited, combine, comb_count, combinations):
    #if vertex not in visited:
        #visited.add(vertex)
    visited.add(vertex)
    for j in graph[vertex]:
        print(vertex)
        if j not in visited:
            combine.add(j)
            dfs_visit(vertex, graph, visited, combine, comb_count)
        combine.pop(comb_count) 
        calcula(combine, combinations)

def firstOnes(myGraph):
    k = set(())
    v = set(())
    #first = set(())
    for i in myGraph:
        #print("\ni: ", i)
        v.update(myGraph[i])
        #print("values: ", v)
        k.add(i)
        print("\nIndex",i,": ", k,"-->", v)
        k.difference_update(v)
        print("\nNew key(s): ", k)
    return list(k)

def calcula(sorvetes, combinations):
    i = 0
    j = i+1
    k = j+1
    for i in sorvetes:
        for j in sorvetes:
            twosum = tuple((i, j))
            combinations.add(twosum)
            for k in sorvetes:
                threesum = tuple((i, j, k))
                combinations.add(threesum) 

#dfs('frutas_cristalizadas', myGraph)

for i in myGraph:
    print("key - value:")
    print("key: ", i, " --> ", "value: ", myGraph[i])
    # print("Tipo myGraph[i]: ", type(myGraph[i]))
    # print("Tipo myGraph.get(i): ", type(myGraph.get(i)))

print(firstOnes(myGraph))
print(keys)
# for i in myGraph:
#     print("key - value:")
#     print("key: ", i, " --> ", "value: ", myGraph.get(i))