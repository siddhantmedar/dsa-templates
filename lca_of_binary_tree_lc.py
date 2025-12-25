class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        def LCA(root, p ,q):
            if not root:
                return root
        
            if root == p or root == q:
                return root

            left = LCA(root.left,p,q)
            right = LCA(root.right,p,q)

            if left and right:
                return root
            
            return left if left else right
        
        return LCA(root, p, q)