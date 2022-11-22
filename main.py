# class Vertex:
#     #connections = []
#     def __init__(self, name):
#         self.name = name
#         self.connections = []
    
#     def add(self, name):
#         self.connections.append(name)

# class Graph:
#     def __init__(self, dict):
#         self.dict = dict 


myGraph = {}

with open('caso2.txt', 'r') as file:
    
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

print("Dicionário:\n", myGraph)

global twosum_count
global threesum_count
#twosum_count = 0
#threesum_count = 0

def dfs(g):    
    visited = set(())
    combine = []
    combinations = set(())
    #combinations_three = set(())      # [...,i,j,k,...]
    #combinations_two = set(())  
    combine_count = 0 
    twosum_count = 0
    threesum_count = 0
    objective = firstOnes(g)
    for v in objective:
        print("\nIndice: ",i)
        dfs_visit(v, g, visited, combine, combine_count, combinations)
    print("\nTotal de combinações de sorvetes: ")#, combinations)
    for e in combinations:
        if len(e) == 2: 
            twosum_count += 1
        else: 
            threesum_count += 1
        print("\n", e)
    print("\nTotal de combinacoes de 2 sabores: ", twosum_count)
    print("\nTotal de combinacoes de 3 sabores: ", threesum_count)
    
def dfs_visit(vertex, graph, visited, combine, combine_count, combinations): 
    visited.add(vertex)
    combine.append(vertex)
    combine_count += 1
    print("\nSabor: ", vertex)
    print("Combinacoes: ", combine)
    for j in graph[vertex]:
        if j not in visited:
            dfs_visit(j, graph, visited, combine, combine_count, combinations)
        elif j in visited and j not in combine:
            dfs_visit(j, graph, visited, combine, combine_count, combinations)  
    calcula(combine, combinations)
    combine.pop(combine.index(vertex))
    combine_count -= 1
    return vertex

def firstOnes(myGraph):
    k = set(())
    v = set(())
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
            #twosum_count += 1
            print(twosum)
            #print(twosum_count)
            for k in range(j+1, len(sorvetes)):
                threesum = tuple((sorvetes[i], sorvetes[j], sorvetes[k]))
                combinations.add(threesum)
                #threesum_count += 1 
                print(threesum)
                #print(threesum_count)


for i in myGraph:
    print("key - value:")
    print("key: ", i, " --> ", "value: ", myGraph[i])
    # print("Tipo myGraph[i]: ", type(myGraph[i]))
    # print("Tipo myGraph.get(i): ", type(myGraph.get(i)))

print(firstOnes(myGraph))
objetivo = firstOnes(myGraph)
print("\nObjevtive: ",objetivo)
#dfs_visit('flocos', graph, visited, combine, combine_count = 0)
dfs(myGraph)
