import sys
import os as my_dir

#class Graph:


#listForGraph = []

class Vertex:
    #connections = []
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def add(self, name):
        self.connections.append(name)



# def __init__(self, vertexes):
#     self.vertexes = {}

# def addInGraph(self, dict, vertex, connection):
#     if dict[vertex] == None:
#         dict[vertex] = Graph.Vertex(vertex)
#     dict[vertex].addConnetion(connection)




# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
#         def dfs(root, targetSum, path):
#             if root == None: return None
            
#             targetSum -= root.val
#             path.append(root.val)
            
#             if root.left == None and root.right == None:
#                 if targetSum == 0:
#                     ans.append(path.copy())
                
#             else:
#                 dfs(root.left, targetSum, path)
#                 dfs(root.right, targetSum, path)
            
#             path.pop()
            
#         ans = []    
#         dfs(root, targetSum, [])
#         return ans