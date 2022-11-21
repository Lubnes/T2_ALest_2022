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

graph = {'frutas_cristalizadas': set(['nata']),
         'nata': set([]),
         'tutti_frutti': set(['passas_ao_rum', 'abÃ³bora']),
         'passas_ao_rum': set(['abÃ³bora']),
         'abÃ³bora': set(['menta']),
         'menta' : set([]),
         'tamarindo': set(['sonho_de_valsa']),
         'sonho_de_valsa': set([]),
         'flocos': set(['tutti_frutti', 'tamarindo', 'sonho_de_valsa'])}

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

visited = set()
combine = []
combinations = set(())


def dfs(g):
    #visited = []       
    #visited = set(())  DESCOMENTAR
    #combs = []
    #combinations = set(())
    #combinations_three = []      # [...,i,j,k,...]
    #combinations_two = []
    combinez = []   
    combine_counter = 0  
    objective = firstOnes(g)
    for v in objective:
        print("\nIndice: ",i)
        dfs_visit(v, g, visited, combine, combine_counter, combinations)
    # if k not in visited:
    #     dfs_visit(k, myGraph)
    print("Combinações de sorvetes: ", combinations)
    
def dfs_visit(vertex, graph, visited, combine, combine_count):#, combinations): DESCOMENTAR
    #if vertex not in visited:
        #visited.add(vertex)
    visited.add(vertex)
    print("Vertex: ", vertex)
    print("Ordem: ", combine)
    combine.append(vertex)
    combine_count += 1
    for j in graph[vertex]:
        if j not in visited:
            #combine.append(j)
            #combine_count += 1
            dfs_visit(j, graph, visited, combine, combine_count)#, combinations)   DESCOMENTAR
        #combine.pop(comb_count) 
    calcula(combine, combinations)
    combine.pop(combine.index(vertex))
    combine_count -= 1
    return vertex

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
    #i = 0
    #j = i+1
    #k = j+1
    for i in range(len(sorvetes)):
        for j in range(i+1,len(sorvetes)):
            twosum = tuple((sorvetes[i], sorvetes[j]))
            combinations.add(twosum)
            print(twosum)
            for k in range(j+1, len(sorvetes)):
                threesum = tuple((sorvetes[i], sorvetes[j], sorvetes[k]))
                combinations.add(threesum) 
                print(threesum)

for i in myGraph:
    print("key - value:")
    print("key: ", i, " --> ", "value: ", myGraph[i])
    # print("Tipo myGraph[i]: ", type(myGraph[i]))
    # print("Tipo myGraph.get(i): ", type(myGraph.get(i)))

print(firstOnes(myGraph))
objetivo = firstOnes(myGraph)
print("\nObjevtive: ",objetivo)
dfs_visit("flocos", graph, visited, combine, combine_count = 0)
