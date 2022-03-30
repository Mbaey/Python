# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = p.val
        b = q.val
        if a > b:
            a,b = b,a
        
        while root:
            val = root.val
            if a <= val and val <=b:
                return root
            elif a <= val and val >=b:
                root = root.left
            elif a >= val and val <=b:
                root = root.right

        return None
