import sys

def main():
    file = open("caso1.txt", "r")
    
    for()

class Graph:
    graph = {}

    def build_graph(graph):
        nodes = []





class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None: return None
            
            targetSum -= root.val
            path.append(root.val)
            
            if root.left == None and root.right == None:
                if targetSum == 0:
                    ans.append(path.copy())
                
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            
            path.pop()
            
        ans = []    
        dfs(root, targetSum, [])
        return ans