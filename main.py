from graph import Vertex


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
print(myGraph)

# parent = {s: None}
# def dfs(adjacencies, start):
#     for v in adjacencies[s]:
#         if v not in parent:
#             parent[v] = s
#             dfs(adjacencies, s)

# color={}
# parent={}
# dfs_output={}
# #inicio 
# for node in myGraph.keys():
#     #print(node)
#     color [node]= "branco"
#     parent[node]= "none"
# print(color)
# print(parent)
# print(myGraph.keys())

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

visited = set(())

combs = set(())
#three_combs = []      # [...,i,j,k,...]

def dfs(start_key, myGraph):
    for k in keys:
        if k not in visited:
            #visited.append(k)
            dfs_visit(start_key, visited)
    print(combs)
    
def dfs_visit(vertex, visited):
    sorvetes = [] #continuar
    if vertex not in visited:
        visited.add(vertex)
        for v in myGraph[vertex]:
            if v not in visited:
                sorvetes.append(v)
                dfs_visit(v, visited)
                calcula(sorvetes)

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

dfs('frutas_cristalizadas', myGraph)