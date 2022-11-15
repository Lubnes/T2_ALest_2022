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

color={}
parent={}
dfs_output={}
#inicio 
for node in myGraph.keys():
    color [node]= "branco"
    parent[node]= "none"
print(color)
print(parent)
print(myGraph.keys())

def dfs(vertice):
    color[vertice]="cinza"
    dfs_output.append(vertice)
    for sabor in myGraph[vertice]:#sabor adjacente ao vertice 
        if color[sabor] == "branco":
            parent[sabor]=vertice
            dfs(sabor)
    color[vertice] = "preto"

dfs("flocos")      
