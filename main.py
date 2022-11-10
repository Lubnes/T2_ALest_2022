import sys
import os as my_dir

def main():
    # my_dir.chdir('../TrabalhoDois')
    # for f in my_dir.listdir():    
    #     print(f)
    my_graph = {}
    with open('../TrabalhoDois/caso1.txt', 'r') as file:
        
        f = file.readlines()

        # while r != None:
        #     print(r, end = '')
        #     r = file.readline()


    
    for line in f:

        words = line.replace('\n', '').split(' -> ')
        print(words)
        a = words[0]
        b = words[1]
        print(a,b)

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