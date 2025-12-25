# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #annotate parent
        
        def dfs(node, parent = None):
            if node:
                node.par = parent

                dfs(node.left, node)
                dfs(node.right, node)
        
        
        dfs(root)
        
        q  = deque([(target, 0)])
        visited = {target}
        
        while q:
            if q[0][1] == k:
                return [node.val for node, d in q]
            else:
                node, d = q.popleft()
                for nd in (node.left, node.right, node.par):
                    if nd and nd not in visited:
                        visited.add(nd)
                        q.append((nd, d+1))
        return []