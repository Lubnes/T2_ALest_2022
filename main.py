import sys
import os as my_dir

def main():
    # my_dir.chdir('../TrabalhoDois')
    # for f in my_dir.listdir():    
    #     print(f)

    myGraph = {}
    listForGraph = []

    with open('../TrabalhoDois/caso1.txt', 'r') as file:
        
        f = file.readlines()

        # while r != None:
        #     print(r, end = '')
        #     r = file.readline()


    
    for line in f:

        words = line.replace('\n', '').split(' -> ')
        key = words[0]
        value = words[1]
        myGraph.setdefault(key, []).extend(value)
        if value not in myGraph:
            myGraph.setdefault(value, [])
        myGraph[words[0]] = words[1]
        print(words)
        #print(a,b)

    print(myGraph)
#class Graph:
#    graph = {}
#
#    def build_graph(graph):
#        nodes = []

main()


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